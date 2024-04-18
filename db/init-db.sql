-- Connect to the database
\c rsvp_app;

-- Create the rsvps table
CREATE TABLE rsvps (
    id SERIAL PRIMARY KEY,
    name VARCHAR2(100) NOT NULL,
    attending VARCHAR2(10) NOT NULL,
    vegetarian VARCHAR2(10),
    plus_one VARCHAR2(10),
    plus_one_name VARCHAR2(100),
    plus_one_vegetarian VARCHAR2(10),
    song_suggestion VARCHAR2(200)
);

CREATE TABLE evening_rsvps (
    id SERIAL PRIMARY KEY,
    name VARCHAR2(100) NOT NULL,
    attending VARCHAR2(10) NOT NULL,
    plus_one VARCHAR2(10),
    plus_one_name VARCHAR2(100)
);
