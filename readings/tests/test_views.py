from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class TestLogin(TestCase):
    """
    Checking if a user can log in or not on the website
    User account first needs to be made before they can log in otherwise the website will redirect to another page
    """

    def test_user_not_logged_redirect(self):
        """
        Checking for a status code of 200 should fail because it should redirect the user away
        """
        response = self.client.get(reverse('reading-list'))
        self.assertEqual(response.status_code, 302)

    def test_view_reading_list(self):
        """
        Logging in a user and checking if they can access the reading-list view
        reading-list view will redirect users to login page if they haven't logged in or there is no session ID
        """
        self.client.force_login(User.objects.get_or_create(username='bobby')[0])
        response = self.client.get(reverse('reading-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'readings/reading_list.html')

    def test_create_new_book(self):
        """
        Checking if a new book can be added onto the website's database
        A user must be logged in to be able to access this page
        Once data has been submitted, the user is redirected to the reading-list view
        """
        self.client.force_login(User.objects.get_or_create(username='bobby')[0])
        data = {'title': 'new book', 'author': 'shawn', 'genre': 'comedy',
                'pages': '100'}
        response = self.client.post(reverse('create-book'), data=data)
        self.assertEquals(response.status_code, 302)
