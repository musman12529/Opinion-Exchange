# API Test Documentation

## Login Page

- **URL:** [http://localhost:8080/start](http://localhost:8080/start)
- **Description:** The login page where users can enter their credentials.

## Forgot Password Page

- **URL:** [http://localhost:8080/forgot](http://localhost:8080/forgot) (method: GET)
- **Description:** The forgot password page where users can reset their passwords.

## Registration Page

- **URL:** [http://localhost:8080/register](http://localhost:8080/register) (method: GET)
- **Description:** The registration page for new users.

## User Registration Endpoint

- **URL:** [http://localhost:8080/register](http://localhost:8080/register) (method: POST)
- **Parameters:** `username` and `password` in the form data.
- **Description:** Registers a new user with the provided username and password.

## User Login Endpoint

- **URL:** [http://localhost:8080/login](http://localhost:8080/login) (method: POST)
- **Parameters:** `username` and `password` in the form data.
- **Description:** Authenticates a user based on provided credentials.

## Home Page

- **URL:** [http://localhost:8080/home](http://localhost:8080/home)
- **Description:** The home page displaying reviews if the user is logged in.

## Settings Page

- **URL:** [http://localhost:8080/settings](http://localhost:8080/settings) (method: GET)
- **Description:** User settings page where users can update their information.

## Update Password Endpoint

- **URL:** [http://localhost:8080/update-password](http://localhost:8080/update-password) (method: POST)
- **Parameters:** `old_password`, `new_password`, and `confirm_password` in the form data.
- **Description:** Updates the user password based on the provided old and new passwords.

## Create Draft Endpoint

- **URL:** [http://localhost:8080/create-draft](http://localhost:8080/create-draft) (method: POST)
- **Parameters:** `topic`, `body`, `anonymous`, `draft`, and `team_id` in the form data.
- **Description:** Creates a new draft review.

## My Drafts Page

- **URL:** [http://localhost:8080/mydrafts](http://localhost:8080/mydrafts) (method: GET)
- **Description:** Page displaying a list of drafts created by the logged-in user.

## Modify Draft Endpoint

- **URL:** [http://localhost:8080/modify-draft](http://localhost:8080/modify-draft) (method: POST)
- **Parameters:** `body` and `review_id` in the form data.
- **Description:** Modifies the content of a draft review.

## Delete Draft Endpoint

- **URL:** [http://localhost:8080/delete-draft](http://localhost:8080/delete-draft) (method: POST)
- **Parameters:** `review_id` in the form data.
- **Description:** Deletes a draft review.

## Create Comment Endpoint

- **URL:** [http://localhost:8080/create-comment](http://localhost:8080/create-comment) (method: POST)
- **Parameters:** `review_id`, `comment`, `criteria1`, `criteria2`, `criteria3`, `criteria4`, `criteria5` in the form data.
- **Description:** Creates a comment on a review with optional criteria ratings.

## Search Endpoint

- **URL:** [http://localhost:8080/search](http://localhost:8080/search) (method: POST)
- **Parameters:** `query` in the form data.
- **Description:** Searches for reviews based on the provided topic/query.

## Add User To Team Endpoint

- **URL:** [http://localhost:8080/addUserToTeam](http://localhost:8080/addUserToTeam) (method: POST)
- **Parameters:** `username`, `team_id` in the form data.
- **Description:** Adds a user to a team.

## Stylesheet

- **URL:** [http://localhost:8080/styles.css](http://localhost:8080/styles.css)
- **Description:** The CSS stylesheet for styling the web pages.
