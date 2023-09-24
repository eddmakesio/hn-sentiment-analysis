CREATE TABLE IF NOT EXISTS story (
    story_id            INTEGER     PRIMARY KEY,
    hn_story_id         INTEGER     NOT NULL,
    title               TEXT        NOT NULL,
    created             DATETIME    NOT NULL
);

CREATE TABLE IF NOT EXISTS comment (
    comment_id          INTEGER     PRIMARY KEY,
    hn_comment_id       INTEGER     NOT NULL,
    contents            TEXT        NOT NULL,
    created             DATETIME    NOT NULL,
    sentiment           FLOAT
);

CREATE TABLE IF NOT EXISTS comment_story (
    comment_story_id    INTEGER     PRIMARY KEY,
    hn_story_id         INTEGER     NOT NULL        REFERENCES story(hn_story_id),
    hn_comment_id       INTEGER     NOT NULL        REFERENCES comment(hn_comment_id)
);
