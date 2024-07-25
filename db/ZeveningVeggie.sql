-- Connect to the database
\c rsvp_app;

ALTER TABLE evening_rsvps 
    ADD vegetarian VARCHAR(10),
    ADD plus_one_vegetarian VARCHAR(10)
;