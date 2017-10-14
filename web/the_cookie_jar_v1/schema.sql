DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS posts;

CREATE TABLE IF NOT EXISTS users (
    id          INTEGER PRIMARY KEY,
    username    TEXT NOT NULL,
    password    TEXT NOT NULL,
    email       TEXT,
    created_at  TIMESTAMP
);

CREATE TABLE IF NOT EXISTS posts (
    id              INTEGER PRIMARY KEY,
    title           TEXT NOT NULL,
    slug            TEXT NOT NULL,
    content         TEXT NOT NULL,
    created_at      TIMESTAMP NOT NULL,
    author          INTEGER NOT NULL,
    FOREIGN KEY (author) REFERENCES users(id)
);

INSERT INTO users(id, username, password, email, created_at) VALUES(1, "admin", "2ab96390c7dbe3439de74d0c9b0b1767", "admin@awesomedev.com", "2017-10-10 13:37:37");
INSERT INTO users(id, username, password, email, created_at) VALUES(2, "user", "1b0612645a677cd4a257212e53285d4c", "user@awesomedev.com", "2017-10-10 13:37:37");
INSERT INTO users(id, username, password, email, created_at) VALUES(3, "dev", "88e2b06179e2e9291b5a8276c94e6402", "dev@awesomedev.com", "2017-10-10 13:37:37");

INSERT INTO posts(id, title, slug, content, created_at, author) VALUES(
    1, "Hello World!", "hello-world", "hello world cool text", "2017-10-10 15:14:54", 1);
INSERT INTO posts(id, title, slug, content, created_at, author) VALUES(
    2, "Cool post", "cool-post", "cool post text", "2017-10-10 16:11:24", 1);
INSERT INTO posts(id, title, slug, content, created_at, author) VALUES(
    3, "Awesome code", "awesome-code", "I have written such awesome code", "2017-10-10 19:05:14", 1);
INSERT INTO posts(id, title, slug, content, created_at, author) VALUES(
    4, "Clean Code", "clean-code", "Remember to write clean code when programming, very important!", "2017-10-10 19:05:14", 1);
INSERT INTO posts(id, title, slug, content, created_at, author) VALUES(
    5, "FINTECH", "fintech", "Working with finicial technologies is very cool and rewarding", "2017-10-10 19:05:14", 1);
INSERT INTO posts(id, title, slug, content, created_at, author) VALUES(
    6, "Crazy dazy", "crazy-dazy", "Damn, writing login functions is difficult, I don't understand sessions that well.", "2017-10-10 19:05:14", 1);
INSERT INTO posts(id, title, slug, content, created_at, author) VALUES(
    7, "Hacked?", "hacked", "Hmmm...I don't know if I have been hacked, how do I check that?", "2017-10-10 19:05:14", 1);
