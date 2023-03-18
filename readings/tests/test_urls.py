from django.test import SimpleTestCase
from django.urls import reverse, resolve
from readings.views import ReadingList, Book, CreateBook, UpdateBook, DeleteBook, UserLogin, RegisterUser


class TestURLS(SimpleTestCase):
    """
    Checking URLS to see if they match views
    """
    def test_reading_list_url_resolves(self):
        url = reverse('reading-list')
        self.assertEqual(resolve(url).func.view_class, ReadingList)

    def test_book_view_url_resolves(self):
        url = reverse('book', args=['12'])
        self.assertEqual(resolve(url).func.view_class, Book)

    def test_create_book_url_resolves(self):
        url = reverse('create-book')
        self.assertEqual(resolve(url).func.view_class, CreateBook)

    def test_update_book_url_resolves(self):
        url = reverse('update-book', args=['15'])
        self.assertEqual(resolve(url).func.view_class, UpdateBook)

    def test_delete_book_url_resolves(self):
        url = reverse('delete-book', args=['7'])
        self.assertEqual(resolve(url).func.view_class, DeleteBook)

    def test_user_login_url_resolves(self):
        url = reverse('user-login')
        self.assertEqual(resolve(url).func.view_class, UserLogin)

    def test_register_user_url_resolves(self):
        url = reverse('register-user')
        self.assertEqual(resolve(url).func.view_class, RegisterUser)
