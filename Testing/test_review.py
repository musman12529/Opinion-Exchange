import unittest

from review import ReviewCollection, ReviewItem, Team, Comment

class TestReviewCollection(unittest.TestCase):
    def test_review_collection(self):
        review_collection = ReviewCollection()
        count = len(review_collection.reviews_all()) # Number of reviews in the initial reviewlist
        userCount = len(review_collection.reviews_by_username(2)) # Number of reviews by our test user

        # Creating/Adding a review
        review_item = ReviewItem(None, "This is a review.", "Topic 1", True, [], 2, True, None)
        review_collection.add_review(review_item)
        review_item = None
        review_list = review_collection.reviews_all()
        self.assertEqual(len(review_list), count+1) # check that the length of the updated reviewlist has increased by 1

        # Retrieving reviews by username
        user_reviews = review_collection.reviews_by_username(2)
        self.assertEqual(len(user_reviews), userCount + 1) # check that the number of test user reviews has increased by 1

        # Updating a review's body
        review_item = review_collection.reviews_by_id("Topic 1")
        review_item.set_body("Updated review", 2)
        self.assertEqual(review_item.get_body(), "Updated review")
        
        # Checking the draft and anonymousity of a review (Clinton Sprint 3)
        self.assertEqual(review_item.get_anonymous(), True)
        self.assertEqual(review_item.get_draft(), True)

        #Deleting a review
        review_collection.remove_review(review_item)
        self.assertEqual(len(review_collection.reviews_all()), count) # check that the length of updated reviewlist is back to it's initial state 

       
    def test_number_of_user_reviews(self):
        review_collection = ReviewCollection()

        # No reviews for a user
        self.assertEqual(review_collection.number_of_user_reviews(300), "No reviews yet")

        # Adding a review to another user
        review_item = ReviewItem(None, "Another review.", "Topic 2", None, [], 1, False, None)
        review_collection.add_review(review_item)
        self.assertEqual(review_collection.number_of_user_reviews(1), 2)
        review_item = review_collection.reviews_by_id("Topic 2")
        review_collection.remove_review(review_item)

class TestReviewItem(unittest.TestCase):
    def test_get_body(self):
        # Test the get_body method of ReviewItem
        review_item = ReviewItem(1, "Test Body", "Test Topic",  None, [], False, "Test Author")
        self.assertEqual(review_item.get_body(), "Test Body")


class TestComment(unittest.TestCase):
    def test_get_body(self):
        # Test the get_body method of Comment
        comment = Comment(1, "Test Comment", 123)
        self.assertEqual(comment.get_body(), "Test Comment")

    def test_invalid_comment_creation(self):
        # Test creating a Comment with invalid input
        with self.assertRaises(TypeError):
            comment = Comment(1, 123, 124)

    def test_not_equal_comments(self):
        # Test inequality of two comments
        comment1 = Comment(None, "Comment 1", 456)
        comment2 = Comment(None, "Comment 2", 789)
        self.assertNotEqual(comment1.get_body(), comment2.get_body())


class TestTeam(unittest.TestCase):
    def test_get_name(self):
        # Test the get_name method of Team
        team = Team(1, "2023-01-01", "Test Team")
        self.assertEqual(team.get_name(), "Test Team")

    def test_invalid_team_creation(self):
        # Test creating a Team with invalid input
        with self.assertRaises(TypeError):
            team = Team(1, "2023-01-01", 2)
    
    def test_not_equal_teams(self):
        # Test inequality of two teams
        team1 = Team(1, "2023-01-01", "Team 1")
        team2 = Team(2, "2023-01-02", "Team 2")
        self.assertNotEqual(team1.get_name(), team2.get_name())


    # Add more test cases for other methods in Team


if __name__ == "__main__":
    unittest.main()
