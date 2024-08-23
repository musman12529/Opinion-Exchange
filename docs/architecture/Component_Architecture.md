+---------------------------+
|      Web Server          |
|     (server.py)          |
|---------------------------|
| - Routes for:             |
|   - Authentication       |
|   - Registration          |
|   - Draft CRUD operations |
|   - Comment creation      |
|   - Review searching      |
|   - Average ratings       |
|   - Team-related actions  |
|   - User settings         |
| - Uses Bottle framework   |
| - Imports:                |
|   - bottle                |
|   - review                |
|   - login_logic           |
|   - data                  |
|   - SessionMiddleware     |
+---------------------------+
            |
            | Uses
            |
            v
+---------------------------+
| User Authentication and  |
| Registration Component   |
| (login_logic.py)          |
|---------------------------|
| - Manages authentication  |
|   and registration        |
| - Functions:              |
|   - check_credentials     |
|   - register_account       |
+---------------------------+
            |
            | Tests
            |
            v
+---------------------------+
| Session Management       |
| Component                 |
| (session_testing.py)      |
|---------------------------|
| - Provides session tests  |
|   for web server          |
| - Tests:                  |
|   - Session creation      |
|   - Multiple sessions     |
|   - Session timeout       |
+---------------------------+
            |
            | Tests
            |
            v
+---------------------------+
| Login Logic Testing       |
| Component                 |
| (login_testing.py)        |
|---------------------------|
| - Contains unit tests for |
|   login logic component   |
| - Tests:                  |
|   - Incorrect credentials |
|   - Correct credentials   |
|   - Successful registration|
|   - Existing username     |
|   - Password mismatch     |
+---------------------------+
            |
            | Uses
            |
            v
+---------------------------+
| Database Component        |
| (data.py)                 |
|---------------------------|
| - Manages database        |
| - Additional functions:   |
|   - CRUD operations for   |
|     user data, teams,     |
|     and user-team         |
|     relationships         |
| - Tests:                  |
|   - Test1                 |
|   - Test2                 |
+---------------------------+
            |
            | Uses
            |
            v
+---------------------------+
| Review Handling Component |
| (review.py)               |
|---------------------------|
| - Manages reviews         |
| - Additional functions:   |
|   - Create, Read, Update, |
|     Delete reviews        |
|   - Search reviews        |
|   - Calculate average     |
|     criteria scores       |
|   - User reviews          |
|   - Add user to team       |
| - Tests:                  |
|   - Test3                 |
|   - Test4                 |
+---------------------------+
