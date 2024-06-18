-- Connect to the database
\c rsvp_app;

ALTER TABLE rsvps 
    ADD wine VARCHAR(10),
    ADD plus_one_wine VARCHAR(10)
;