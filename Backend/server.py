from bottle import route, run, request, template, static_file, redirect, app
import review
import json
import login_logic
import data
from beaker.middleware import SessionMiddleware

HOST_NAME = "localhost"
SERVER_PORT = 8080

reviews = review.ReviewCollection()
totalreviews = reviews.reviews_all()


def session_timeout_handler(session):
    print("Session expired for user:", session.get('username'))
    redirect('/start')


session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 3000,
    'session.data_dir': './data',
    'session.auto': True,
    'session.timeout_handler': session_timeout_handler
}

app = SessionMiddleware(app(), session_opts)


class ReviewHandler:
    """
        Class responsible for managing reviews and user sessions.

        Attributes:
            reviews (ReviewCollection): Collection of reviews.
            totalreviews (list): List of all reviews.
            count (int): Review count.
            LoggedInUser (dict): Details of the logged-in user.
            reviewItem (ReviewItem): Current review item being created or modified.
        """

    reviews = review.ReviewCollection()
    totalreviews = reviews.reviews_all()
    count = 0
    LoggedInUser = None
    reviewItem = None



    @classmethod
    def insert_rating(cls, user_id, review_id, criteria1, criteria2, criteria3, criteria4, criteria5):
        """
        Insert a rating into the database with five criteria scores.

        Args:
            user_id (int): The ID of the user submitting the rating.
            review_id (int): The ID of the review being rated.
            criteria1 (int): The score for criteria1.
            criteria2 (int): The score for criteria2.
            criteria3 (int): The score for criteria3.
            criteria4 (int): The score for criteria4.
            criteria5 (int): The score for criteria5.

        Returns:
            int: The ID of the inserted rating or None if insertion failed.
        """
        data.create_rating(criteria1, criteria2, criteria3, criteria4, criteria5, review_id, user_id)


    @classmethod
    def get_ratings_by_review_id(cls, review_id):
        """
        Get ratings made to a particular review by review ID.

        Args:
            review_id (int): The ID of the review.

        Returns:
            list: A list of dictionaries containing rating details.
                  Each dictionary includes the following keys:
                  - "id" (int): The ID of the rating.
                  - "review_id" (int): The ID of the review being rated.
                  - "user_id" (int): The ID of the user who submitted the rating.
                  - "criteria1" (int): The score for criteria1.
                  - "criteria2" (int): The score for criteria2.
                  - "criteria3" (int): The score for criteria3.
                  - "criteria4" (int): The score for criteria4.
                  - "criteria5" (int): The score for criteria5.
        """
        review_ratings = data.get_ratings_by_review_id(review_id)
        rating_list = []

        for rating in review_ratings:
            rating_dict = {
                "id": rating['id'],
                "review_id": rating['review_id'],
                "user_id": rating['user_id'],
                "criteria1": rating['criteria1'],
                "criteria2": rating['criteria2'],
                "criteria3": rating['criteria3'],
                "criteria4": rating['criteria4'],
                "criteria5": rating['criteria5']
            }
            rating_list.append(rating_dict)

        return rating_list

    @classmethod
    def get_ratings_by_user_id(cls, user_id):
        """
        Get ratings made by a particular user by user ID.

        Args:
            user_id (int): The ID of the user.

        Returns:
            list: A list of dictionaries containing rating details.
                  Each dictionary includes the following keys:
                  - "id" (int): The ID of the rating.
                  - "review_id" (int): The ID of the review being rated.
                  - "user_id" (int): The ID of the user who submitted the rating.
                  - "criteria1" (int): The score for criteria1.
                  - "criteria2" (int): The score for criteria2.
                  - "criteria3" (int): The score for criteria3.
                  - "criteria4" (int): The score for criteria4.
                  - "criteria5" (int): The score for criteria5.
        """
        user_ratings = data.get_ratings_by_user_id(user_id)
        rating_list = []

        for rating in user_ratings:
            rating_dict = {
                "id": rating['id'],
                "review_id": rating['review_id'],
                "user_id": rating['user_id'],
                "criteria1": rating['criteria1'],
                "criteria2": rating['criteria2'],
                "criteria3": rating['criteria3'],
                "criteria4": rating['criteria4'],
                "criteria5": rating['criteria5']
            }
            rating_list.append(rating_dict)
        return rating_list

    @classmethod
    def load_all(cls):

        """
                Load and retrieve all reviews as a list of dictionaries.

                Returns:
                    list: A list of review dictionaries containing relevant information.
        """

        cls.reviews = review.ReviewCollection()
        cls.totalreviews = cls.reviews.reviews_all()
        init_list = []
        cls.count = len(init_list)
        for item in cls.totalreviews:
            init_list.append({"getbody": item.getBody(), "getID": item.getID(), "getTopic": item.getTopic(),
                              "getCommnents": item.getComments(), "getAuthor": item.getAuthor()})

        return init_list

    @classmethod
    def create(cls, topic, body, team_id=0):
        """
        Create a new review.

        Args:
            topic (str): The topic of the review.
            body (str): The review content.
            team_id (int): The team ID for private comments (default is 0).
        """
        session = request.environ.get('beaker.session')
        user = session['user']
        if data.get_user(session.get('user')["username"]):
            if team_id == 0:
                cls.reviewItem = review.ReviewItem(None, body, topic, None, user["id"], 0)
                cls.reviews.add_review(cls.reviewItem)
                cls.reviewItem = None
            else:
                cls.reviewItem = review.ReviewItem(None, body, topic, None, user["id"], team_id)
                cls.reviews.add_review(cls.reviewItem)
                cls.reviewItem = None

    @classmethod
    def add_user_to_team(cls, owner_user_id, user_id_to_add, team_id):
        """
        Add a user to the team if the owner is authorized.

        Args:
            owner_user_id (int): The ID of the team owner.
            user_id_to_add (int): The ID of the user to add.
            team_id (int): The ID of the team.

        Returns:
            str: A message indicating the result of the operation.

        """
        # Clinton Sprint 3 code
        session = request.environ.get('beaker.session')
        user = session['user']
        if data.get_user(session.get('user')["username"]):
            if user["id"] != owner_user_id:
                return "Only the team owner can add users to the team."
        try:
            # Attempt to add the user to the team
            data.add_user_to_team(user_id_to_add, team_id)
            
            return "pass"
        except Exception as e:
            # Handle specific database-related error (e.g., IntegrityError for duplicate entries)
            if "UNIQUE constraint failed" in str(e):
                return "User is already a member of this team."
            else:
                print(e)
                return "An error occurred while adding the user to the team."
        #
    @classmethod
    def calculate_average_criteria(cls, review_id):
        """
        Calculate the average criteria scores for a given review.

        Args:
            cls: The ReviewHandler class.
            review_id (int): The ID of the review.

        Returns:
            list: A list containing the average scores for each criterion.

        Each element in the list corresponds to the average score for the following criteria:
            criteria1 (int): The average score for criteria1.
            criteria2 (int): The average score for criteria2.
            criteria3 (int): The average score for criteria3.
            criteria4 (int): The average score for criteria4.
            criteria5 (int): The average score for criteria5.
        """
        ratings = cls.get_ratings_by_review_id(review_id)
        criteria1_ratings = []
        criteria2_ratings = []
        criteria3_ratings = []
        criteria4_ratings = []
        criteria5_ratings = []

        for rating in ratings:
            criteria1_ratings.append(rating['criteria1'])
            criteria2_ratings.append(rating['criteria2'])
            criteria3_ratings.append(rating['criteria3'])
            criteria4_ratings.append(rating['criteria4'])
            criteria5_ratings.append(rating['criteria5'])

        criteria1_average = round(sum(criteria1_ratings) / (len(criteria1_ratings) or 1), 1)
        criteria2_average = round(sum(criteria2_ratings) / (len(criteria2_ratings) or 1), 1)
        criteria3_average = round(sum(criteria3_ratings) / (len(criteria3_ratings) or 1), 1)
        criteria4_average = round(sum(criteria4_ratings) / (len(criteria4_ratings) or 1), 1)
        criteria5_average = round(sum(criteria5_ratings) / (len(criteria5_ratings) or 1), 1)

        return [criteria1_average, criteria2_average, criteria3_average, criteria4_average, criteria5_average]

    @classmethod
    def user_reviews(cls, user_id):
        """
        Retrieve reviews created by a specific user.

        Args:
            cls: The ReviewHandler class.
            user_id (int): The ID of the user.

        Returns:
            list: A list of review items created by the specified user.
        """
        mydraft_init = []
        init_list = ReviewHandler.load_all()
        for item in init_list:
            if item["getAuthor"]["id"] == user_id:
                mydraft_init.append(item)
        return mydraft_init

    @classmethod
    def modify_draft(cls, text, review_id):
        """
        Modify the content of a draft review.

        Args:
            cls: The ReviewHandler class.
            text (str): The updated review content.
            review_id (int): The ID of the review to modify.
        """
        session = request.environ.get('beaker.session')
        user = session['user']
        if data.get_user(session.get('user')["username"]):
            for item in cls.totalreviews:
                a = item.get_id()
                if int(a) == int(review_id):
                    item.set_body(text, user["id"])

    @classmethod
    def delete_draft(cls, review_id):
        """
        Delete a draft review.

        Args:
            cls: The ReviewHandler class.
            review_id (int): The ID of the review to delete.
        """
        for item in cls.totalreviews:
            a = item.get_id()
            if int(a) == int(review_id):
                cls.reviews.remove_review(item)

    @classmethod
    def search_topic(cls, topic):
        """
        Search for reviews by topic.

        Args:
            cls: The ReviewHandler class.
            topic (str): The topic to search for.

        Returns:
            list: A list of review items matching the specified topic.
        """
        mydraft_init = []
        init_list = ReviewHandler.load_all()
        for item in init_list:
            if item["getTopic"] == topic:
                mydraft_init.append(item)
        return mydraft_init

    @classmethod
    def create_comment(cls, review_id, comment):

        """
                Create a new review.


                Args:
                    review_id (str): The topic of the review.
                    comment (str): The review content.

        """
        session = request.environ.get('beaker.session')
        user = session['user']
        if data.get_user(session.get('user')["username"]):
            for item in cls.totalreviews:
                a = item.get_id()
                if int(a) == int(review_id):
                    item.add_comment(a, user["id"], comment)
                    print(a)
    #


@route('/')
@route('/start')
def login():
    """
        Display the login page.

        Returns:
            str: HTML template for the login page.
    """

    return template('login')
@route('/forgot')
def forgot_password():
    """
    Display the forgot password page.

    Returns:
        str: HTML template for the forgot password page.
    """
    return template('forgot')


@route('/forgot', method='POST')
def forgot_password():
    """
    Handle the forgot password functionality.
    """
    username = request.forms.get('username')
    new_password = request.forms.get('newPassword')

    # Check if the username exists in the server
    existing_user = data.get_user(username)

    if existing_user:
        # Update the password for the user
        data.update_user(existing_user['id'], username, new_password, existing_user['token'])
        return "Password reset successful. <a href='/start'>Login</a>"
    else:
        return "Username not found. <a href='/forgot'>Try again</a>"

@route('/register')
def register():
    """
        Display the register page.

        Returns:
            str: HTML template for the register page.
    """

    return template('register')


# For sprint 2
@route('/register', method='POST')
def do_register():
    """
    Handle user registration.

    Returns:
        str: Result message with HTML link(s) for redirection.
    """
    username = request.forms.get('username')
    password = request.forms.get('password')
    confirm_password = request.forms.get('confirm_password')

    if password != confirm_password:
        return "Registration failed. Password and Confirm Password do not match. <a href='/register'>Try again</a>"

    existing_user = data.get_user(username)
    if existing_user:
        return "Registration failed. Username is already taken. <a href='/register'>Try again</a>"

    data.create_user(username, password)
    return "Registration successful. <a href='/start'>Login</a>"



@route('/login', method='POST')
def do_login():
    """
    Handle user login.

    Returns:
        str: Result message with HTML link(s) for redirection.
    """
    username = request.forms.get('username')
    password = request.forms.get('password')

    if login_logic.check_credentials(username, password):
        session = request.environ.get('beaker.session')
        user = data.get_user(username)
        session['user'] = user

        print(
            f'Session created for user: {session["user"]} with a timeout of {session_opts["session.cookie_expires"]} seconds')
        redirect('/home')
    else:
        return "Login failed. Invalid username or password. <a href='/register'>Register</a>"


@route('/home')
def init_page():
    """
    Display the home page.

    Returns:
        str: HTML template for the home page.
    """
    session = request.environ.get('beaker.session')
    user = data.get_user(session.get('user')["username"])
    
    if user:
        selectedTeam = int(request.query.get('selectedTeam', 0))
        teams = data.get_teams_by_user_id(user["id"])
    
        if selectedTeam == 0:
            totalreviews = reviews.reviews_all()
            average_criterias = []
            for review in totalreviews:
                average_criterias.append(ReviewHandler.calculate_average_criteria(review_id=review.get_id()))

        else:
            totalreviews = reviews.reviews_by_team(selectedTeam)
        
        return template('home_template', reviews = totalreviews, average_criterias = average_criterias, teams = teams, selectedTeam = selectedTeam)

    else:
        redirect('/start')


@route('/create-draft', method='POST')
def createDraft():
    """
    Handle creating a draft review.
    """
    session = request.environ.get('beaker.session')
    user = session.get('user')
    if user:
        anonymous = request.forms.get('anonymous') == 'on'
        topic = request.forms.get('topic')
        body = request.forms.get('body')
        draft = request.forms.get('draft') == 'on'
        team_id = int(request.forms.get('team_id'))
        if anonymous:
            user = data.get_user("Anonymous")
            reviewItem = review.ReviewItem(None, body, topic, draft, None, user["id"], anonymous, team_id)
        else:
            reviewItem = review.ReviewItem(None, body, topic, draft, None, user["id"], anonymous, team_id)

        print(anonymous)
        reviews.add_review(reviewItem)
        
        referring_url = request.get_header('Referer')
        if referring_url:
            redirect(referring_url)
    else:
        redirect('/start')


@route('/mydrafts', method="GET")
def mydrafts():
    """
    Display the user's draft reviews.

    Returns:
        str: HTML template for the user's draft reviews.
    """
    session = request.environ.get('beaker.session')
    user = session['user']

    if data.get_user(session.get('user')["username"]):
        items = reviews.reviews_by_username(user["id"])
        return template('my_drafts', reviews=items)
    else:
        redirect('/start')


@route('/modify-draft', method="POST")
def modify():
    """
    Handle modifying a draft review.
    """
    body = request.forms.get('body')
    review_id = request.forms.get('review_id')
    ReviewHandler.modify_draft(body, review_id)
    redirect('/mydrafts')


@route('/delete-draft', method="POST")
def delete():
    """
    Handle deleting a draft review.
    """
    review_id = request.forms.get('review_id')
    ReviewHandler.delete_draft(review_id)
    redirect('/mydrafts')


@route('/create-comment', method="POST")
def create_comment():
    """
    Handle creating a comment on a review.
    """
    comment = request.forms.get('comment')
    session = request.environ.get('beaker.session')
    user = session.get('user')
    review_id = request.forms.get('review_id')
    criteria1 = request.forms.get('criteria1')
    criteria2 = request.forms.get('criteria2')
    criteria3 = request.forms.get('criteria3')
    criteria4 = request.forms.get('criteria4')
    criteria5 = request.forms.get('criteria5')
    
    dbcomment = review.ReviewItem.add_comment(review_id, user["id"], comment)
    print(dbcomment)
    data.create_rating(review_id, user['id'], dbcomment, criteria1, criteria2, criteria3, criteria4, criteria5)
    redirect('/home')

@route('/search', method='POST')
def search_item():
    """
    Handle searching for reviews by topic.
    Returns:
        str: HTML template for displaying search results.
    """
    query = request.forms.get('query')

    session = request.environ.get('beaker.session')
    user = session['user']
    if data.get_user(user['username']):
        items = ReviewHandler.searchTopic(query)
        sun_json = json.dumps(items)
        return template('home_template', sun=sun_json)
    else:
        redirect('/start')

# Clinton Sprint 3 code
@route('/addUserToTeam', method='POST')
def add_user_to_team():
    session = request.environ.get('beaker.session')
    user = session.get('user')
    owner_id = user['id']
    username = request.forms.get('username')
    user_data = data.get_user(username)
    team_id = int(request.forms.get('team_id'))
    print(owner_id, team_id)

    if username != "Anonymous":
        if team_id != 0:
            if user and user_data:
                user_id = user_data['id']
                a = ReviewHandler.add_user_to_team(owner_id, user_id, team_id)
                if a != "pass":
                    return a
                else:
                    referring_url = request.get_header('Referer')
                    if referring_url:
                        redirect(referring_url)

            else:
                return f"User {username} could not be added to the team"
        else:
            return f"Users are added to the global domain by default"
    else:
        return f"User could not be added to the team"
    #


@route('/settings')
# server.py

@route('/settings')
def settings():
    """
    Display the user settings page.

    Returns:
        str: HTML template for the user settings page.
    """
    session = request.environ.get('beaker.session')
    user = data.get_user(session.get('user')["username"])
    password = data.get_user(session.get('user')['passwordHash'])

    if user:
        return template('settings_template', user=user, passwordHash=password)
    else:
        redirect('/start')



@route('/update-password', method='POST')
def update_password():
    """
    Handle updating the user password.

    Returns:
        str: Result message with HTML link(s) for redirection.
    """
    session = request.environ.get('beaker.session')
    user = session.get('user')

    old_password = request.forms.get('old_password')
    new_password = request.forms.get('new_password')
    confirm_password = request.forms.get('confirm_password')

    if login_logic.check_credentials(user['username'], old_password):
        if new_password == confirm_password:
            data.update_user(user['id'], user['username'], new_password, user['token'])
            return "Password updated successfully. <a href='/settings'>Go back to settings</a>"
        else:
            return "Password update failed. New password and confirm password do not match. <a href='/settings'>Try again</a>"
    else:
        return "Password update failed. Incorrect old password. <a href='/settings'>Try again</a>"







@route('/styles.css', method="GET")
def css():
    """
        Serve the CSS file for styling.

        Returns:
            str: CSS file content.
    """

    return static_file('styles.css', root='.')

if __name__ == "__main__":
    run(app=app, host=HOST_NAME, port=SERVER_PORT)
