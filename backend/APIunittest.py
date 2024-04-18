import unittest
from flask import Flask
from flask_testing import TestCase
from flask_sqlalchemy import SQLAlchemy
from app import app, db, rsvps

class APITestCase(TestCase):
    # Define rsvp_data_john and rsvp_data_jane at the class level
    rsvp_data_john = {
        'name': 'John Doe',
        'attending': 'Yes',
        'vegetarian': 'No',
        'plus_one': 'Yes',
        'plus_one_name': 'Johns Wife',
        'plus_one_vegetarian': 'Yes',
        'song_suggestion': 'Song 1'
    }

    rsvp_data_jane = {
        'name': 'Jane Doe',
        'attending': 'No',
        'vegetarian': 'Yes',
        'plus_one': 'No',
        'plus_one_name': '',
        'plus_one_vegetarian': 'No',
        'song_suggestion': 'Song 2'
    }

    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory SQLite
        self.db = db
        return app

    def setUp(self):
        self.db.create_all()  # Use the new db instance

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_create_rsvp(self):

        response = self.client.post('/rsvp', json=self.rsvp_data_john)
        self.assertStatus(response, 201)
        self.assertEqual(response.json, {'message': 'RSVP created successfully'})

    def test_get_all_rsvps(self):
        rsvp1 = rsvps(**self.rsvp_data_john)
        rsvp2 = rsvps(**self.rsvp_data_jane)
        db.session.add_all([rsvp1, rsvp2])
        db.session.commit()

        response = self.client.get('/rsvps')
        self.assertStatus(response, 200)
        self.assertEqual(response.json, [
            {
                'id': rsvp1.id,
                'name': 'John Doe',
                'attending': 'Yes',
                'vegetarian': 'No',
                'plus_one': 'Yes',
                'plus_one_name': 'Johns Wife',
                'plus_one_vegetarian': 'Yes',
                'song_suggestion': 'Song 1'
            },
            {
                'id': rsvp2.id,
                'name': 'Jane Doe',
                'attending': 'No',
                'vegetarian': 'Yes',
                'plus_one': 'No',
                'plus_one_name': '',
                'plus_one_vegetarian': 'No',
                'song_suggestion': 'Song 2'
            }
        ])

if __name__ == '__main__':
    unittest.main()