CREATE TABLE questions (
    question_id INTEGER PRIMARY KEY,
    question VARCHAR(255) NOT NULL,
    answer VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL
);