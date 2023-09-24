CREATE TABLE IF NOT EXISTS story (
    hn_story_id         INTEGER     PRIMARY KEY,
    title               TEXT        NOT NULL,
    created             INTEGER     NOT NULL,
    UNIQUE(hn_story_id)
);

CREATE TABLE IF NOT EXISTS comment (
    hn_comment_id       INTEGER     PRIMARY KEY,
    contents            TEXT        NOT NULL,
    created             INTEGER     NOT NULL,
    sentiment           FLOAT,
    UNIQUE(hn_comment_id)
);

CREATE TABLE IF NOT EXISTS comment_story (
    comment_story_id    INTEGER     PRIMARY KEY,
    hn_story_id         INTEGER     NOT NULL        REFERENCES story(hn_story_id),
    hn_comment_id       INTEGER     NOT NULL        REFERENCES comment(hn_comment_id),
    UNIQUE(hn_story_id, hn_comment_id)
);
