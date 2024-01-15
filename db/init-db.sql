-- Connect to the database
\c rsvp_app;

-- Create the rsvps table
CREATE TABLE rsvps (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    attending BOOLEAN NOT NULL,
    vegetarian BOOLEAN NOT NULL,
    plus_one VARCHAR(10) NOT NULL,
    plus_one_name VARCHAR(100),
    plus_one_vegetarian BOOLEAN NOT NULL,
    song_suggestion VARCHAR(200)
);
