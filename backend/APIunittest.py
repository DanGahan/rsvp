import unittest
from flask import Flask
from flask_testing import TestCase
from app import app, db, rsvps

class APITestCase(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.init_app(app)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_rsvp(self):
        rsvp_data = {
            'name': 'John Doe',
            'attending': 'Yes',
            'vegetarian': 'No',
            'plus_one': 'Yes',
            'plus_one_name': 'Jane Doe',
            'plus_one_vegetarian': 'Yes',
            'song_suggestion': 'Some song suggestion'
        }

        response = self.client.post('/rsvp', json=rsvp_data)
        self.assertStatus(response, 201)
        self.assertEqual(response.json, {'message': 'RSVP created successfully'})

    def test_get_all_rsvps(self):
        rsvp1 = rsvps(name='John Doe', attending='Yes', vegetarian='No', plus_one='Yes',
                      plus_one_name='Jane Doe', plus_one_vegetarian='Yes', song_suggestion='Song 1')
        rsvp2 = rsvps(name='Jane Doe', attending='No', vegetarian='Yes', plus_one='No',
                      plus_one_name='', plus_one_vegetarian='No', song_suggestion='Song 2')
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
                'plus_one_name': 'Jane Doe',
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