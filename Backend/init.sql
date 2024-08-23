PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS comments;
DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS memberships;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS TEAMS;

CREATE TABLE users (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    passwordHash TEXT,
    token TEXT,
    created DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE TEAMS (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    date_created DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE memberships (
    user_id INTEGER,
    team_id INTEGER,
    PRIMARY KEY (user_id, team_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (team_id) REFERENCES TEAMS(id)
);

CREATE TABLE reviews (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    topic TEXT,
    body TEXT,
    draft INTEGER DEFAULT FALSE,
    author INTEGER,
    team_id INTEGER,
    isAnonymous INTEGER DEFAULT FALSE,
    created DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (author) REFERENCES users(id),
    FOREIGN KEY (team_id) REFERENCES TEAMS(id)
);

CREATE TABLE comments (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    review INTEGER,
    author INTEGER,
    body TEXT,
    created DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (author) REFERENCES users(id),
    FOREIGN KEY (review) REFERENCES reviews(id)
);

CREATE TABLE ratings (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    review_id INTEGER,
    user_id INTEGER,
    comment_id INTEGER,
    criteria1 INT,
    criteria2 INT,
    criteria3 INT,
    criteria4 INT,
    criteria5 INT,
    FOREIGN KEY (review_id) REFERENCES reviews(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
    FOREIGN KEY (comment_id) REFERENCES comments(id)
);



INSERT INTO users (username, passwordHash) VALUES ("zuhair", "password123");
INSERT INTO users (username, passwordHash) VALUES ("clinton", "password123");
INSERT INTO users (username, passwordHash) VALUES ("stephen", "password123");
INSERT INTO users (username, passwordHash) VALUES ("usman", "password123");
INSERT INTO users (username, passwordHash) VALUES ("ibrahim", "password123");
INSERT INTO users (username, passwordHash) VALUES ("Anonymous", "testing");


INSERT INTO TEAMS(name) VALUES ("team A");
INSERT INTO TEAMS(name) VALUES ("team B");
INSERT INTO TEAMS(name) VALUES ("team C");

INSERT INTO reviews (topic, body, author, team_id) VALUES (
    "Stephen's hat",
    "I think Stephen's hat is great. I love the color. How does everyone else feel?",
    1,
    1
);

INSERT INTO reviews (topic, body, author, team_id) VALUES (
    "Clinton's Sprint 1 Performance",
    "What are everyone's thoughts?",
    2,
    1
);

INSERT INTO reviews (topic, body, author) VALUES (
    "Stephen's Sprint 2 Performance",
    "Looking to gauge an overall opinion.",
    2
);

INSERT INTO reviews (topic, body, author) VALUES (
    "Zuhair's overall performance",
    "How does everyone feel about this member?",
    3
);

INSERT INTO comments (review, author, body) VALUES (
    1,
    1,
    "Awesome review. We love to see it."
);

INSERT INTO ratings (review_id, user_id, comment_id, criteria1, criteria2, criteria3, criteria4, criteria5) VALUES (
    1,
    1,
    1,
    1,
    2,
    3,
    4,
    5
);

INSERT INTO memberships(user_id, team_id) VALUES (1, 1);
INSERT INTO memberships(user_id, team_id) VALUES (1, 2);
INSERT INTO memberships(user_id, team_id) VALUES (1, 3);

-- ALTER TABLE reviews
-- ADD COLUMN anonymous INTEGER DEFAULT FALSE
