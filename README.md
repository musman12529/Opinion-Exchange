

# Opinion Exchange

## Video Demonstration



<!-- https://github.com/musman12529/DiscussHub/assets/114633620/846d5025-185b-4fe3-b33c-7520f353b16d -->



## Table of Contents
. Introduction
. Server
. Session Management
. Frontend Framework
. User Login Logic
. App Logic
. Database Logic
. Unit tests
. Prerequisites
. Installation
. Usage
. Other Information

## Default Username and Password
Username: zuhair
Password: password123


## Introduction
This repository contains the source code for a forum app, designed to create and manage discussion forums. The project is divided into several key components, each with its own responsibilities. This README provides an overview of these components and instructions on setting up and running the app.

## Server
The server component of the forum app is responsible for handling HTTP requests, routing pages, and serving web pages. It is also responsible for session management. It interacts with the database, App Logic file, and the Login logic file. It is implemented using the BOTTLE framework.  

## Session Management
The session management is responsible for allowing multiple users to be logged into the server simultaneously. It interacts with the server and the database to get user details. It is implemented using Beaker. 

## Frontend Framework
The frontend framework is responsible for the user interface and user experience of the forum app. It is developed using HTML and CSS. Key features of the frontend framework include:
User-friendly and responsive design.
Forum creation, thread creation, and commenting interfaces.
Private and Public Posts

## User Login Logic
The user login logic is responsible for user authentication and registration. It ensures that pre-registered users can log in and access their profiles. Key features of the user login logic include:
User registration with username and password.
Secure password logic checking and authentication.
User sessions 
Encrypted passwords and tokens for authentication (Future task).

## App Logic
The app logic is at the core of the forum app. It is responsible for defining how the app functions and manages forum-related operations, including forum creation, deletion, modification, and user interactions. Key features of the app logic include:
Classes for Forum creation, modification, and deletion.
User interactions, such as following forums, liking threads, and reporting content. (Future task)
Real-time updates and notifications.
Search functionality for finding specific forums and forums created by the user.
Teams Class that defines the behavior of teams
A Rating Class that defines the behavior of ratings

## Database Logic
The database logic is responsible for managing data storage, retrieval, and manipulation. We use SQLite for storing forum data. Key features of the database logic include:
Schema design for forums, threads, comments, ratings, teams, and users.
Resolution of Many to Many relationships that exist between entities
Data persistence and retrieval.
Database migrations for schema changes and updates.

## Installation

1. Clone the repository:

    ```bash
    git clone (https://github.com/CS2005F23/term-project-teamb.git)
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure the application settings if needed.

## Usage

1. Run the application:

    ```bash
    python server.py
    ```

2. Access the application through your browser at `http://localhost:8080`.

## Features

- **User Management:** Register, log in, update password, and manage user settings.
- **Review Handling:** Create, modify, delete drafts, comment on reviews, and calculate average criteria scores.
- **Team Collaboration:** Add users to teams (for authorized team owners).
- **Search Functionality:** Search reviews by topic.
- **User Sessions:** Session management with a timeout of 3000 seconds.
- **And few other**

## Unit tests
- For server unit test check the Server_Test_Postman.postman_collection.json and Server_Test_Doc.md
- for app logic check test_review.py
- there is also session testing in the session_testing.py
- for other test check server_testing.py

## Docs folder
- In the docs foleder you can find the following for the evaluation:
- Meeting notes can be found in the Docs folder file name is meetingNotes
- Performance reviews are named as performanceReviews.md
- user stories are named as userStories.md
- There is a processAnalysis.md file in there as well.
- Also there is a notes.md file that can tell you about the task and who did which interface design.
  
## Architecture Folder
- Inside the Docs folder there is a Architecture folder that includes files for component architecture and microservice architecture
  

## Coding design and Interface Design For Sprint 3
-Clinton: Applogic Interface Design

-Zuhair: Frontend Interface Design

-Ibrahin: Database Interface Design

-Usman: Server Interface Design

-Stephen: User and Session Mangement Interface Design

Coding tasks were assigned based on the strength of the members, some members worked on more than one interface. Details are in the kanban board
