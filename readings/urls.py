from django.urls import path
from .views import ReadingList, Book, CreateBook, UpdateBook, DeleteBook, UserLogin, RegisterUser, \
    PasswordChange
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views

urlpatterns = [
    # authentication
    path('login/', UserLogin.as_view(), name='user-login'),
    path('logout/', LogoutView.as_view(next_page='user-login'), name='logout'),
    path('register/', RegisterUser.as_view(), name='register-user'),
    path('update-password/', PasswordChange.as_view(), name='update-password'),

    # web navigation and CRUD
    path('', ReadingList.as_view(), name='reading-list'),
    path('book/<int:pk>', Book.as_view(), name='book'),
    path('create-book/', CreateBook.as_view(), name='create-book'),
    path('update-book/<int:pk>/', UpdateBook.as_view(), name='update-book'),
    path('delete-book/<int:pk>/', DeleteBook.as_view(), name='delete-book'),
]