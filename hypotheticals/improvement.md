
------------------------------------------------------------------------------------------------------------------------


## General Team Improvements

# architecture design document

- Change the overall structure of the architectural design by expressively detailing the architectural components of our projects. This would come in the form of graphical diagrams, textual descriptions, or a combination of both. 
- Implement a well thought out microarchitecure deisgn, compare it to server and other architecture design to ensure it is logical.
- Schedule team meetings that solely focuses on establishing a common understanding of the document's purpose, structure, and content requirements.
- Have more consistent meeting and disucssions with the professors, from ALL members. This ensures less confusion.
- Remove inconsistent modules or interfaces
- Consistent Representation: I understand the importance of a cohesive and standardized representation of the architecture. I'll collaborate closely with team members to establish a unified style for presenting the architecture, ensuring that all diagrams adhere to a consistent format. This includes using UML diagrams that accurately depict component interfaces and relationships, avoiding redundancies and inconsistencies.

- Comprehensive Overview: we will revisit the overview document to ensure it comprehensively covers all project components and their interfaces. This includes reconciling any discrepancies between the text description and the diagram representation. The aim is to provide a clear and complete understanding of how my interface design and code fit into the broader project components.

- Clarity in Process Explanation: we will make sure to differentiate between the agile approach we're implementing with multiple sprints and any outdated or irrelevant methodologies like waterfall. This means clearly outlining the elements of our process model and how they align with the iterative nature of our project.

- Correct Usage of Terminology: Addressing the misuse of terms like "deployment," we'll refine the language used in the documentation to accurately reflect the context of our project. Additionally, I'll ensure that any diagrams effectively illustrate the relationships between project elements, providing a clearer visual representation of these connections.


# Unit tests

- Confirm regression testing on PR acceptance.
- All members to look and take time to test and understand unit tests.
- Add many missing unit tests 
- Conglomerate all unit tests into single file to reduce files and clean up directory (mentioned to team in previous sprint but decided not to)
- Do extensive unit testing amongst the team, and ensure each test case is valid.


# Code reviews and Performance review

- More detailed code reviews. - Instead of having (yes this code is good), specifially have code review that denotes what has been changed or added to the code. 
- EX: login_logic updated for hash password, code review stating that method hash_password was added and used in previous functions: check_credentials and register_account. These methods also update the data.py a bit, after reviewing data.py the code looks good. After reading code, went on to test code and cases X,y,Z. Cases X,Y are valid, Case Z is not. Must update code so case Z is valid.
- The above example is a more in depth review than what some of the reviews have been. Even so, the reviews can be more in depth, and should prove to the developer insight on the code.
- If a reviewer says the code is right and its not, causes alot of confusion and trouble for the developr who created it and assumed right based on the false reviews. This happened alot in our code reviews: memebers stated a piece of code was good with little review and in turn caused alot of extra back log and retracking work.
- Ensuring that the code reviews made by team members leads to meaningful outcomes which are documented 
- Fewer pull requests but more branch commits
- Structuring code reviews (Code quality, Functional Review, decoupling, error handling, documentation.). SOLID and DRY falls under the code quality criteria
- For performance review, we would have meetings to discuss on how problems arising as the team progressses could be resolved. We would also create a kanban item for those problems, turn it into an issue and comment on them as the issues are being resolved step by step.

#  Process Model Analysis

- We would conduct a process model analysis as if we were going with the agile sprint method because the project is based off on sprints (Three sprints for this semester)
- "Deployment" does not mean pushing to the master branch, it means deploying the code to a live server and hosting it on the world wide web. We would modify the deployment section on the file.
- Changes in process would be discussed, if there was any.
- - Elements of process identified and explained. Distinction made between process and process model.
- Would like add  a diagram of elements and their relationships..
- Terms like deployment are  being used correctly
- Changes in process since beginning of project are discussed.
-Expected to add more than a few bullet points. What are the new code review elements.
-reimplementation is a not a process element. coding task will be described as process element.
- Changes in process would be discussed, if there was any.


# Microservices Architecture
- We would have implemented a diagram in addition to the document we submitted. 
- A relationship would exist between the gateway and the identified microservices while the Authentication broker relates with the session management. 
- Lastly, we would have implemented a relationship between the data broker and our SQL server.
- In summary, the diagram would be quite similar to the sample microservices document you provided but the changes would be our project's identified microservices linked to the appropriate gateway/broker
------------------------------------------------------------------------------------------------------------------------

## Usman Individual Assignment Improvements

# architecture design document

- Consistent Representation: I understand the importance of a cohesive and standardized representation of the architecture. I'll collaborate closely with team members to establish a unified style for presenting the architecture, ensuring that all diagrams adhere to a consistent format. This includes using UML diagrams that accurately depict component interfaces and relationships, avoiding redundancies and inconsistencies.

- Comprehensive Overview: I'll revisit the overview document to ensure it comprehensively covers all project components and their interfaces. This includes reconciling any discrepancies between the text description and the diagram representation. The aim is to provide a clear and complete understanding of how my interface design and code fit into the broader project components.

- Clarity in Process Explanation: I'll make sure to differentiate between the agile approach we're implementing with multiple sprints and any outdated or irrelevant methodologies like waterfall. This means clearly outlining the elements of our process model and how they align with the iterative nature of our project.

- Correct Usage of Terminology: Addressing the misuse of terms like "deployment," I'll refine the language used in the documentation to accurately reflect the context of our project. Additionally, I'll ensure that any diagrams effectively illustrate the relationships between project elements, providing a clearer visual representation of these connections.

- I'll work diligently to align both the textual and visual representations, ensuring clarity, consistency, and accuracy throughout the documentation.

# Unit tests

- Upon reviewing my postman test results, I discovered discrepancies and errors within some of the tests. To rectify this, I plan to enhance my unit testing approach by completing any missing tests and addressing the issues causing the existing tests to fail. This involves meticulous debugging of my code to ensure that all unit tests run smoothly without errors, thereby improving the reliability and accuracy of my testing process.

# Code reviews and Performance review

- To improve the code review process, I'll implement structured reviews that lead to actionable outcomes. I'll ensure that team members conduct thorough reviews, addressing both style concerns like SOLID and de-coupling, as well as verifying code correctness. To address regression testing gaps, I'll integrate unit tests as a part of the review process, ensuring code changes don't inadvertently affect existing functionalities. Additionally, I'll establish and enforce pull request deadlines, fostering a more disciplined approach to code submission and review. Clear documentation or records summarizing the outcomes of these reviews will be created and maintained, allowing for easy identification of review results and actionable next steps. This structured approach will enhance the code review process, promoting quality, consistency, and collaboration within the team.

# Submission with branch/pull request

- I'll enforce our team's methodology by submitting code changes exclusively through branches and pull requests, preventing direct merges into the master branch. Meeting sprint pull-request deadlines will be a priority to ensure timely reviews and merges. Consistent adherence to these practices will maintain the integrity of our workflow.

# Docstrings 

- To improve docstring , I'll enhance clarity and completeness by expanding descriptions for each module and interface element. I'll ensure consistency, keeping docs updated with code changes and including practical examples where helpful. Exploring documentation tools will streamline the process, making the docstrings an indispensable resource for users.

#  SOLID, de-coupling

- To further improve the code, I'll focus on strengthening SOLID principles, ensuring modules align with Single Responsibility, Open-Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion. Prioritizing de-coupling for minimized interdependencies and implementing patterns like Adapter will enhance flexibility. Consistent adherence to coding standards and industry best practices will elevate overall code quality and maintainability.

#  Task completion

- To elevate the score, I'll prioritize completing all tasks with fully functional code. Additionally, I'll include an attributions table, acknowledging contributions and sources used in the project. This comprehensive approach ensures both task fulfillment and proper crediting for external contributions, enriching the overall quality of the work.
------------------------------------------------------------------------------------------------------------------------=



## Clinton's Improvements

# Product

- My unit tests for Sprint 2 are WORKING, PASSING, CORRECT, test for correct and incorrect test cases and I got an 8/10 (test_review.py)
- docstrings are also completed and well documented and I got a 7
- Improve on the architecural design on my compomemt interface by combining graphical diagrams with textual decriptions
- Remove inconsistent modules or interfaces in the architecural design on my compomemt interface


# Process

- Make sure that commits are made to the master branch through the approved PR methodology. It's currently being implemented in the final sprint. 
- You gave exceptions for improvements on the hypotheticals
- Performance reviews were made by all team members, for all team members. I got a 3
- Ensuring that my code reviews and reviews by other team members on my code leads to meaningful outcomes which are documented.

------------------------------------------------------------------------------------------------------------------------=

## Stephen's Improvements

# Sprint 2 updates - Upgrades performed on Stephen Code based on sprint 2 marking
There were very little updates that I had made on my sprint 2 project after seeing the sprint 2 marking.
After discussing with other members, realized that multiple members got the same individual mark....
This denotes that the marker is not looking at every little detail (which is what the professor told it would be) meaning that no matter how much individual change is done, we will still get a template mark.
Also having a good mark in sprint 2 of 83, decided there was very little that i could improve upon as there were things that i did add to sprint 2 and still did not recieve the marks.
Meaning, even if I did implement these in sprint 3, it was unlikely the marker to in depth mark all the work i have done.
Therefore, decided on simply focusing on sprint 3 tasks.
COPIED FROM INDIVIDUAL MARKING
EX:  
Process
* **3/5 points** Code reviews of your submissions by team members is meaningful and leads to new backlog items where appropriate - I believed my code reviews were more than sufficient... I do not see what more i could have commented
* **3/5 points** Performance review conducted by team and student response where needed. - this is individual marking... why does this sentence entail "team"? Also, i believe i have more than done this by meticulously checking others code and discussing erorrs on many PR's.
* **3/5 points** Submission must be made as a branch/pull request using team approved methodology.  - Although i might have not done this completely properly, I for sure showed effort and tried to follow the methodology as explained by professor in class. 3/5 marks for this makes no sense.
Product
* **5/8 points** Team architecture design document indicates how your interface design and code fits into the overall project components. - Once again... this is supposed to be INDIVIDUAL GRADING: why am i getting marked on this for what the team submitted? I mentioned previously in kanban, documents, and even to professor, and to team: that the architecture should be a single architecture to reduce redundancies. I believe the marking of 5/8 reflects the team grading, not my individual knowledge for this aspect.
* **8/10 points** Unit tests are correct and working (not necessarily passing) for public interface methods/services of your design components and coding tasks, sufficient to test a correct mode and incorrect mode for different method invocations. - My individual unit testing does work and contains valid test cases for my desgin components:
* **7/10 points** Docstrings are complete and appropriate for all modules and public interface elements of your design components and coding tasks - this makes sense, I did not have proper docstrings on login_logic. They are now updated for sprint 3
* **3/5 points** Task completion with finished working code and attributions table - my tasks were complete and i had updated my attribution table, why would i lose marks here?

My final individual grade was 83/100 - EXACTLY THE SAME TO OTHER STUDENTS IN THE TEAM. As explained above, how is the student supposed to increase their skills "individually" if this is how we are getting marked? This "individual" marking scheme portrays the teams' grade rather than the individual stuednts.
Out of these I have outlined above the marks i believe to be in correct or unfairly graded with specific examples of why.
For many of these things, I have already followed the guideline to get 100%, therefore there is very little except doctstrings which i can change which will increase my individual mark.
# Sprint 3 things to improve on:
As disccussed in the userStories.md, there was alot of confusion amongst this last sprint, and little time to stay organized as students were facing many other exams and curriculum.
This led to things being done late, and difficulty on improving and working on the project consistently. Therefore, one of the improvements would to try and manage time better.
I had little time to test all unit testing cases, as well as the POSTMAN. There are certain test cases that are not account for, and should be to improve the server.
The microarchitecture and the architecture designs were a good amount of marks in sprint 3. Was not able to get group together to discuss, so simply created my own in hope that in was correct and entailed all the other developers interfacing.



------------------------------------------------------------------------------------------------------------------------=

