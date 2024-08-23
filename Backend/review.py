import data, data_stub
# data_stub operations are no longer in effect since the data.py tasks are done


class ReviewCollection:
    """
    A class for temporarily storing review items.

    """

    def __init__(self):
        self._reviews = []

    def _create_review_item(self, item):
        comments = [Comment(comment["id"], comment["body"], comment["author"]) for comment in item["comments"]]
        for i in comments:
            print(i.get_body(), i.get_id(), i.get_author())
        return ReviewItem(item["id"], item["body"], item["topic"], item["draft"], comments, item["author"], item["isAnonymous"], item["teamID"])
    def reviews_all(self):
        """
        Retrieve all reviews and add them to the collection.
        """
        review_list = data.get_reviews()
        self._reviews = [self._create_review_item(item) for item in review_list]
        return self._reviews

    def add_review(self, review_item):

        """
        Add a review to the collection.

        Args:
            reviewItem (ReviewItem): The review item to add.
        """
        data.create_review(review_item.get_topic(), review_item.get_body(), review_item.get_author(), review_item.get_draft(),
                           review_item.get_team_id(), review_item.get_anonymous())
        self.reviews_all()

    @staticmethod
    def remove_review(review_item):

        """
        Remove a review from the collection and data source.

        Args:
            reviewItem (ReviewItem): The review item to remove.
        """
        data.remove_review(int(review_item.get_id()))

    def reviews_by_username(self, user):
        """
        Retrieve reviews by a specific user.
        Used for unit Testing

        Args:
            user (str): The username to filter reviews by.

        Returns:
            list: A list of reviews by the specified user.
        """
        review_list = data.get_reviews_by_user(user)
        if review_list:
            return [self._create_review_item(item) for item in review_list]

    def number_of_user_reviews(self, user):
        """
        Get the number of reviews by a specific user.

        Args:
            user (str): The username to count reviews for.

        Returns:
            int: The number of reviews by the specified user or "No reviews yet" if none found.
        """
        reviews = self.reviews_by_username(user)
        return len(reviews) if reviews else "No reviews yet"

    # Sprint 2 Code
    @staticmethod
    def teams_by_user(user):
        """
        Retrieve teams that a specific user belongs to.

        Args:
            user (int): The user ID.

        Returns:
            list: A list of team objects representing the team the user belongs to.
        """
        teams_by_user = data.get_teams_by_user_id(user)
        return [Team(item["id"], item["created"], item["name"]) for item in teams_by_user]

    def reviews_by_team(self, team_id):
        """
        Retrieve reviews for a specific team.

        Args:
            team_id (int): The team ID.

        Returns:
            list: A list of review objects belonging to the team.
        """
        reviews_list = data.get_reviews_by_team_id(team_id)
        return [self._create_review_item(item) for item in reviews_list]

    def reviews_by_id(self, topic):
        """
        Retrieves a review based on it's ID.
        Used for unit testing but can be incorporated into the main code if necessary

        Args:
            ID (int): The ID of the review we want to get.

        Returns:
            item (obj): The reviewItem object containing the ID.
        """
        for item in self._reviews:
            if item.get_topic() == topic:
                return item
        return "Item Not Found"

    @staticmethod
    def ratings_by_review_id(review_id):
        """
        Retrieves ratings made to a particular review

        Args:
            ID (int): The ID of the review we need.

        Returns:
            filteredList (list): A list of rating objects
        """
        init = data.get_ratings_by_review_id(review_id)
        return [Rating(item["id"], item["review_id"], item["user_id"], item["critA"], item["critB"], item["critC"],
                       item["critD"], item["critE"]) for item in init]

    @staticmethod
    def ratings_by_user(user_id):
        """
        Retrieves ratings made by a particular user

        Args:
            ID (int): The ID of the user we need.

        Returns:
            filteredList (list): A list of rating objects
        """
        init = data.get_ratings_by_user_id(user_id)
        return [Rating(item["id"], item["review_id"], item["user_id"], item["critA"], item["critB"], item["critC"],
                       item["critD"], item["critE"]) for item in init]

    #

    def __len__(self):
        return len(self._reviews)

    def __str__(self):
        return f"ReviewCollection with {len(self)} reviews."


class ReviewItem:
    """
    Individual review items for the review class.
    """

    def __init__(self, id, body, topic, draft, comments, author, anonymous,  team_id=None):
        self.id = id
        self.body = body
        self.topic = topic
        self.comments = comments
        self.author = author
        self.team_id = team_id
        self.anonymous = anonymous
        self.draft = draft

    def get_body(self):
        return self.body

    def get_id(self):
        return self.id

    def set_body(self, new_body, user_id):
        """
        Update the review body.

        Args:
            newBody (str): The new body for the review.
            userID (int): the author_id of the current user.
        """
        self.body = new_body
        data.update_review(self.id, self.topic, self.body, user_id, False)

    def get_author(self):
        return self.author

    def get_topic(self):
        return self.topic

    def get_comments(self):
        return self.comments

    # Sprint 2 Code
    def get_team_id(self):
        return self.team_id

    @staticmethod
    def add_comment(review_id, user_id, comment):
        return data.create_comment(review_id, user_id, comment)

    #

    # Sprint 3 Code
    
    def get_anonymous(self):
        return self.anonymous

    def get_draft(self):
        return self.draft
    
    #


# Sprint 2 Code
class Team:
    """
    Team Class that defines the properties of teams (a feature for sprint 2)
    """

    def __init__(self, id, created, name):
        if not isinstance(name, str):
            raise TypeError("Invalid argument types. Name must be a string.")
        self.id = id
        self.created = created
        self.name = name

    def get_created_date(self):
        return self.created

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name


class Rating:
    """
    Rating Class that defines individual ratings made by the user on a review item

    """

    def __init__(self, id, review_id, user_id, critA, critB, critC, critD, critE):
        self.id = id
        self.review_id = review_id
        self.user_id = user_id
        self.critA = critA
        self.critB = critB
        self.critC = critC
        self.critD = critD
        self.critE = critE

    """
    The methods below are getter methods to return the values of the initialised variables

    """

    def get_id(self):
        return self.id

    def get_review_id(self):
        return self.review_id

    def get_user_id(self):
        return self.user_id

    def get_critA(self):
        return self.critA

    def get_critB(self):
        return self.critB

    def get_critC(self):
        return self.critC

    def get_critD(self):
        return self.critD

    def get_critE(self):
        return self.critE


#


class Comment:
    """
    Represents a comment on a review.
    """

    def __init__(self, id, body, author):
        if not isinstance(body, str):
            raise TypeError("Invalid argument types. Body must be a string.")
        self.body = body
        self.author = author
        self.id = id
        if id is not None:
            item = data.get_ratings_by_comment_id(id)
            self.ratings = Rating(item["id"], item["review_id"], item["user_id"], item["criteria1"], item["criteria2"], item["criteria3"], item["criteria4"], item["criteria5"])

    def get_body(self):
        return self.body

    def get_author(self):
        return self.author

    def get_id(self):
        return self.id
    
    def get_ratings(self):
        return self.ratings
