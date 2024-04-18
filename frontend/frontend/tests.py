# frontend/tests.py
import json
from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch

class FrontendViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    @patch('requests.get')  # Mock the requests.get function
    def test_get_all_rsvps_view(self, mock_get):
        mock_response = {
            'count': 2,
            'results': [
                {'name': 'John', 'attending': True, 'vegetarian': False},
                {'name': 'Jane', 'attending': False, 'vegetarian': True},
            ]
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        response = self.client.get(reverse('get_all_rsvps'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'all_rsvps.html')

    def test_header_view(self):
        response = self.client.get(reverse('header_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'header.html')
        # Add more assertions as needed

    def test_footer_view(self):
        response = self.client.get(reverse('footer_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'footer.html')
        # Add more assertions as needed

    def test_form_view(self):
        response = self.client.get(reverse('form_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'form.html')
        # Add more assertions as needed

    def test_success_page_view(self):
        response = self.client.get(reverse('success_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'success.html')
        # Add more assertions as needed

    @patch('requests.post')  # Mock the requests.post function
    def test_submit_data_view(self, mock_post):
        mock_post.return_value.status_code = 201

        response = self.client.post(
            reverse('submit_data'),
            {
                'name': 'John Doe',
                'attending': True,
                'vegetarian': False,
                'plus_one': 'Yes',
                'plus_one_name': 'Jane Doe',
                'plus_one_vegetarian': True,
                'song_suggestion': 'A nice song',
            }
        )

        self.assertEqual(response.status_code, 302)  # Expecting a redirect after successful submission
        self.assertRedirects(response, reverse('success_page'))
        # Add more assertions as needed
