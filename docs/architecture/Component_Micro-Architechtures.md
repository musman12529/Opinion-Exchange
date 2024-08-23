1) Web Server (server.py):

Responsible for handling HTTP requests and managing routes.
Uses the Bottle framework for web development.

Imports modules:
- bottle
- review
- login_logic
- data
- SessionMiddleware

2) User Authentication and Registration Component (login_logic.py):

Manages user authentication and registration.

Functions:
- check_credentials: Validates user credentials for login.
- register_account: Registers a new user account.

3) Session Management Component (session_testing.py):

Provides tests for session management in the web server.

Tests:
- Session creation.
- Handling multiple sessions.
- Session timeout.
- User Logout

4) Login Logic Testing Component (login_testing.py):

Contains unit tests for the login logic component.

Tests:
- Incorrect credentials.
- Correct credentials.
- Successful registration.
- Existing username.
- Password mismatch.

5) Database Component (data.py):

Manages database interactions.

Additional functions:
- CRUD operations for user data, teams, and user-team relationships.

6) Review Handling Component (review.py):

Manages reviews and related operations.

Additional functions:
- Create, Read, Update, Delete reviews.
- Search reviews.
- Calculate average criteria scores.
- Retrieve user reviews.
- Add a user to a team.
- Comment Creation
- Ratings Functionality

## Comparison: 
- Each microservice can be scaled independently based on demand while the existing approach requires the entire application to be scaled, limiting flexibility 
- Each microservice can be developed, deployed, and maintained independently, reducing dependency concerns while with the existing approach, changes in one component can affect the entire system
- Microservice architecture can be implemented using different technologies while component-based architecture is tied to a single development stack, reducing new technologies. 
- The component-based architecture is easier to develop due to its centralized codebase but the microservice architecture introduces complexity when it comes to inter-service communication, data consistency, and deployment. 

## Impact on team Software Process:
Development Approach:
- Microservices: Teams can work independently on different microservices, allowing for parallel development and faster iteration.
- Monolithic: A centralized codebase may require more coordination among teams and slower development cycles due to interdependencies.

Team Collaboration:
- Microservices: Teams work on smaller, focused services, enabling better specialization and autonomy.
- Monolithic: Teams might face challenges in ownership and collaboration due to a shared codebase.

Unit Testing and Maintenance:
- Microservices: Requires comprehensive testing strategies for individual services and intricate coordination for end-to-end testing.
- Monolithic: Easier end-to-end testing but might face challenges in pinpointing issues due to the interconnected nature of the application.

In conclusion, transitioning from a component-based architecture to a microservices architecture offers advantages in terms of scalability, agility, and technology flexibility but also introduces complexities in terms of distributed system management and coordination among teams. Teams need to adapt their processes, tools, and communication strategies to effectively work within a microservices ecosystem.


