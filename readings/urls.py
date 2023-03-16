from django.urls import path
from .views import ReadingList, Book, CreateBook, UpdateBook, DeleteBook

urlpatterns = [
    path('', ReadingList.as_view(), name='reading-list'),
    path('book/<int:pk>', Book.as_view(), name='book'),
    path('create-book/', CreateBook.as_view(), name='create-book'),
    path('update-book/<int:pk>/', UpdateBook.as_view(), name='update-book'),
    path('delete-book/<int:pk>/', DeleteBook.as_view(), name='delete-book'),
]