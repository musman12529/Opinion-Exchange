import sqlite3
import hashlib
import os
from login_logic import hash_password

con = sqlite3.connect('data.db')
cur = con.cursor()

# Clinton Sprint 3 code (more adherence to DRY principle)
def reviews_iterator(reviews):
    """
    An iterator that returns an arbitrary number of reviews based on the input
    
    Args:
    reviews: from the database

    Returns a list of review dictionaries
    """
    reviews_list = []
    if len(reviews) > 0:
        for review in reviews:
            comments = cur.execute("SELECT * FROM comments WHERE review=?", [review[0]]).fetchall()
            comments_list = []

            user = cur.execute("SELECT * FROM users WHERE id=?", [review[4]]).fetchone()
            review_author = {
                "id": user[0],
                "username": user[1]
            }
            if len(comments) > 0:
                for comment in comments:
                    user = cur.execute("SELECT * FROM users WHERE id=?", [comment[2]]).fetchone()
                    author = {
                        "id": user[0],
                        "username": user[1]
                    }
                    comment_dict = {
                        "id": comment[0],
                        "author": author,
                        "body": comment[3],
                        "created": comment[4]
                    }
                    comments_list.append(comment_dict)

            review_dict = {
                "id": review[0],
                "body": review[2],
                "topic": review[1],
                "comments": comments_list,
                "author": review_author,
                "draft": bool(review[3]),
                "teamID": review[5],
                "isAnonymous": bool(review[6]) 
                # "created": review[7]
            }
            reviews_list.append(review_dict)

    return reviews_list
    #

def initialize_database():
    """
    Initialize the database tables if they don't exist.

    Reads and executes the SQL script from 'init.sql' to create tables.
    """
    with open('init.sql', 'r') as sql_file:
        sql_script = sql_file.read()

    listOfTables = cur.execute(
        """SELECT name FROM sqlite_master WHERE type='table' """).fetchall()

    if not all(table_name in listOfTables for table_name in
               [('users',), ('reviews',), ('comments',), ('TEAMS',), ('memberships',)]):
        cur.executescript(sql_script)
        con.commit()


def get_reviews():
    """
    Retrieve all reviews and their associated comments from the database.

    Returns:
    List of review dictionaries.
    """
    reviews = cur.execute("SELECT * FROM reviews").fetchall()
   

    return reviews_iterator(reviews=reviews)


def get_reviews_by_user(user_id=""):
    """
    Retrieve reviews by a specific topic.

    Args:
    topic (str): The topic to filter reviews.

    Returns:
    List of review dictionaries.
    """
    reviews = cur.execute("SELECT * FROM reviews WHERE author == ?", [user_id]).fetchall()
    

    return reviews_iterator(reviews=reviews)



def get_reviews_by_topic(topic=""):
    """
    Retrieve reviews by a specific topic.

    Args:
    topic (str): The topic to filter reviews.

    Returns:
    List of review dictionaries.
    """
    reviews = cur.execute("SELECT * FROM reviews WHERE topic == ?", [topic]).fetchall()
    
    return reviews_iterator(reviews=reviews)


def update_review(id, topic, body, author_id, draft):
    """
    Update a review in the database.

    Args:
    id (int): The ID of the review to update.
    topic (str): The updated topic.
    body (str): The updated body.
    author_id (int): The author's ID.
    draft (int): 0 if not a draft, 1 if a draft.

    """
    cur.execute("UPDATE reviews SET topic = ?, body = ?, author = ?, draft = ? WHERE id = ?;",
                [topic, body, author_id, draft, id])
    con.commit()


def create_review(topic, body, author_id, draft, team_id, anonymous):
    """
    Create a new review in the database.

    Args:
    topic (str): The topic of the review.
    body (str): The body of the review.
    author_id (int): The author's ID.
    draft (int): 0 if not a draft, 1 if a draft.
    team_id (int): The ID of the team associated with the review.
    """
    cur.execute("INSERT INTO reviews (topic, body, author, draft, team_id, isAnonymous) VALUES (?, ?, ?, ?, ?, ?)",
                [topic, body, author_id, draft, team_id, anonymous])
    con.commit()


def remove_review(id):
    """
    Remove a review from the database.

    Args:
    id (int): The ID of the review to remove.
    """
    cur.execute("DELETE FROM reviews WHERE id = ?", [id])
    con.commit()


def create_comment(review_id, Author_id, body):
    """
    Create a comment for a review in the database.

    Args:
    review_id (int): The ID of the review to comment on.
    author_id (int): The author's ID.
    body (str): The body of the comment.

    """
    cur.execute("INSERT INTO comments (review, author, body) VALUES (?, ?, ?)",
                [review_id, Author_id, body])
    con.commit()
    return cur.lastrowid


def get_user(username):
    """
    Retrieve user information from the database.

    Args:
    username (str): The username of the user to retrieve.

    Returns:
    User dictionary.
    """
    user = cur.execute("SELECT * FROM users where username = ?", [username]).fetchone()
    if user:
        user_dict = {
            "id": user[0],
            "username": user[1],
            "passwordHash": user[2],
            "token": user[3],
            "created": user[4]
        }
        return user_dict
    else:
        return None



def create_user(username, password):
    """
    Create a new user in the database.

    Args:
    username (str): The username of the user.
    password (str): The plain text password of the user.

    Note: The provided password will be hashed before saving it to the database.
    """
    salt = hashlib.sha256(os.urandom(32)).hexdigest().encode('ascii')
    hashed_password = hash_password(password, salt)

    # Store the hashed password as a blob
    cur.execute("INSERT INTO users (username, passwordHash) VALUES (?, ?)", [username, hashed_password])
    con.commit()


def update_user(id, username, passwordHash, token):
    """
    Update user in the database.

    Args:
    id (int): The ID of the user to update.
    username (str): The updated username.
    passwordHash (str): The updated password hash.
    token (str): The updated token.
    """
    cur.execute("UPDATE users SET username = ?, passwordHash = ?, token = ? WHERE id = ?",
                [username, passwordHash, token, id])
    con.commit()


def remove_user(id):
    """
    Remove a user fromitialize_database() the database.

    Args:
    id (int): The ID of the user to remove.
    """
    cur.execute("DELETE FROM users WHERE id = ?", [id])
    con.commit()


def get_reviews_by_team_id(team_id):
    """
    Retrieve reviews by a specific team id.

    Args:
    team_id (int): The team id to filter reviews.

    Returns:
    List of review dictionaries.
    """
    reviews = cur.execute("SELECT * FROM reviews WHERE team_id = ?", [team_id]).fetchall()
    return reviews_iterator(reviews=reviews)

    

def get_users_by_team_id(team_id):
    """
    Get all users that belong to a specific team.

    Args:
    team_id (int): The ID of the team.

    Returns:
    List of user dictionaries.
    """
    users = cur.execute("""
        SELECT u.id, u.username FROM users u
        INNER JOIN memberships m ON u.id = m.user_id
        WHERE m.team_id = ?
    """, (team_id,)).fetchall()

    return [{"id": user[0], "username": user[1]} for user in users]


def get_teams_by_user_id(user_id):
    """
    Get all users that belong to a specific team.

    Args:
    team_id (int): The ID of the team.

    Returns:
    List of user dictionaries.
    """
    teams = cur.execute("""
        SELECT * FROM TEAMS t
        INNER JOIN memberships m ON t.id = m.team_id
        WHERE m.user_id = ?
    """, (user_id,)).fetchall()

    return [{"id": team[0], "name": team[1], "created": team[2]} for team in teams]


def add_user_to_team(user_id, team_id):
    """
    Add a user to a team by creating a membership record.

    Args:
    user_id (int): The ID of the user.
    team_id (int): The ID of the team.
    """
    cur.execute("INSERT INTO memberships (user_id, team_id) VALUES (?, ?)", (user_id, team_id))
    con.commit()


def create_rating(review_id: object, user_id: object, comment_id: object, criteria1: object, criteria2: object, criteria3: object, criteria4: object, criteria5: object) -> object:
    """
    Create a rating associated with a review, a comment, and a user.

    Args:
    review_id (int): The ID of the associated review.
    user_id (int): The ID of the user making the review.
    comment_id (int): The ID of the associated comment.
    criteria1, criteria2, criteria3, criteria4, criteria5 (int): The scores for the predefined criteria.
    """
    cur.execute(
        "INSERT INTO ratings (review_id, user_id, comment_id, criteria1, criteria2, criteria3, criteria4, criteria5) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (review_id, user_id, comment_id, criteria1, criteria2, criteria3, criteria4, criteria5))
    con.commit()


def get_ratings_by_review_id(review_id):
    """
    Return a list of ratings made to a particular review ID.

    Args:
    review_id (int): The ID of the review.

    Returns:
    List of dictionaries, each containing rating details.
    """
    ratings = cur.execute("SELECT * FROM ratings WHERE review_id = ?", (review_id,)).fetchall()
    return [
        {'id': rating[0], 'review_id': rating[1], 'user_id': rating[2], 'comment_id': rating[3], 'criteria1': rating[4],
         'criteria2': rating[5], 'criteria3': rating[6], 'criteria4': rating[7], 'criteria5': rating[8]} for rating in
        ratings]


def get_ratings_by_user_id(user_id):
    """
    Return a list of ratings made by a particular user ID.

    Args:
    user_id (int): The ID of the user.

    Returns:
    List of dictionaries, each containing rating details.
    """
    ratings = cur.execute("SELECT * FROM ratings WHERE user_id = ?", (user_id,)).fetchall()
    return [{'id': rating[0], 'review_id': rating[1], 'user_id': rating[2], 'comment_id': rating[3], 'criteria1': rating[4], 'criteria2': rating[5], 'criteria3': rating[6], 'criteria4': rating[7], 'criteria5': rating[8]} for rating in ratings]


def get_ratings_by_comment_id(comment_id):
    """
    Return a list of ratings made by a particular user ID.

    Args:
    user_id (int): The ID of the user.

    Returns:
    List of dictionaries, each containing rating details.
    """
    rating = cur.execute("SELECT * FROM ratings WHERE comment_id = ?", (comment_id,)).fetchone()
    return {'id': rating[0], 'review_id': rating[1], 'user_id': rating[2], 'comment_id': rating[3], 'criteria1': rating[4], 'criteria2': rating[5], 'criteria3': rating[6], 'criteria4': rating[7], 'criteria5': rating[8]}






initialize_database()
#create_user('q', 'q')
# create_review("topic", "body", 1, False)
# print(get_reviews())
