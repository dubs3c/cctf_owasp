DROP TABLE IF EXISTS posts;

CREATE TABLE IF NOT EXISTS posts (
    id              INTEGER PRIMARY KEY,
    title           TEXT NOT NULL,
    slug            TEXT NOT NULL,
    content         TEXT NOT NULL,
    created_at      TIMESTAMP NOT NULL,
    published       INTEGER NOT NULL,
    author          INTEGER NOT NULL
);

INSERT INTO posts(id, title, slug, content, created_at, published, author) VALUES(
    0, "Hello wrlx!", "Ooops", "CCTF{0ut_0f_s1ght_out_0f_m1nd}", "1987-13-26 13:37:00", 0, 1);
INSERT INTO posts(id, title, slug, content, created_at, published, author) VALUES(
    1, "Hello World!", "hello-world", "hello world cool text", "2017-10-10 15:14:54", 1, 1);
INSERT INTO posts(id, title, slug, content, created_at, published, author) VALUES(
    2, "Cool post", "cool-post", "cool post text", "2017-10-10 16:11:24", 0, 1);
INSERT INTO posts(id, title, slug, content, created_at, published, author) VALUES(
    3, "Awesome code", "awesome-code", "I have written such awesome code", "2017-10-10 19:05:14", 1, 1);
INSERT INTO posts(id, title, slug, content, created_at, published, author) VALUES(
    4, "Clean Code", "clean-code", "Remember to write clean code when programming, very important!", "2017-10-10 19:05:14", 1, 1);
INSERT INTO posts(id, title, slug, content, created_at, published, author) VALUES(
    5, "FINTECH", "fintech", "Working with finicial technologies is very cool and rewarding", "2017-10-10 19:05:14", 0, 1);
INSERT INTO posts(id, title, slug, content, created_at, published, author) VALUES(
    6, "Crazy dazy", "crazy-dazy", "Writing a blog is so easy! I wonder how I delete things...", "2017-10-10 19:05:14", 1, 1);
INSERT INTO posts(id, title, slug, content, created_at, published, author) VALUES(
    7, "Hacked?", "hacked", "Hmmm...I don't know if I have been hacked, how do I check that?", "2017-10-10 19:05:14", 1, 1);
INSERT INTO posts(id, title, slug, content, created_at, published, author) VALUES(
    8, "Hmmm?", "tips", "What did an array start at again....? Am I using matlab? No of course not!", "2017-10-15 13:15:24", 0, 1);
