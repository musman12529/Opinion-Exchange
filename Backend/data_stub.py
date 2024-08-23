# data_stub.py

def get_teams_by_user_id(user_id):
    # Stub implementation: Returns a predefined list of teams for the user
    return [
        {"id": 1, "created": "2023-01-01", "name": "Team 1"},
        {"id": 2, "created": "2023-01-02", "name": "Team 2"},
    ]

def get_reviews_by_user(user):
    # Stub implementation: Returns a predefined list of reviews by user
    return [
        {"id": 1, "body": "Review 1 Body", "topic": "Review 1", "comments": [], "author": user},
        {"id": 2, "body": "Review 2 Body", "topic": "Review 2", "comments": [], "author": user},
    ]

def get_reviews_by_team_id(team_id):
    # Stub implementation: Returns a predefined list of reviews for the team
    return [
        {"id": 1, "body": "Team Review 1 Body", "topic": "Team Review 1", "comments": [], "author": "Team Author 1"},
        {"id": 2, "body": "Team Review 2 Body", "topic": "Team Review 2", "comments": [], "author": "Team Author 2"},
    ]

def create_comment(review_id, user_id, comment):
    # Stub implementation: Prints a message indicating the creation of a comment
    print(f"Comment '{comment}' added to review with ID {review_id} by user with ID {user_id}.")

def get_ratings_by_review_id(review_id):
    # Stub implementation: Returns a predefined list of ratings for a review
    return [
        {"id": 1, "review_id": review_id, "user_id": 1, "critA": 5, "critB": 4, "critC": 3, "critD": 5, "critE": 2},
        {"id": 2, "review_id": review_id, "user_id": 2, "critA": 3, "critB": 4, "critC": 5, "critD": 2, "critE": 4},
    ]

def get_ratings_by_user_id(user_id):
    # Stub implementation: Returns a predefined list of ratings by user
    return [
        {"id": 1, "review_id": 1, "user_id": user_id, "critA": 4, "critB": 3, "critC": 5, "critD": 2, "critE": 4},
        {"id": 2, "review_id": 2, "user_id": user_id, "critA": 5, "critB": 4, "critC": 3, "critD": 5, "critE": 2},
    ]
