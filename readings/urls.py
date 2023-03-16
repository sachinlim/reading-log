from django.urls import path
from .views import ReadingList, Book, CreateBook

urlpatterns = [
    path('', ReadingList.as_view(), name='reading-list'),
    path('book/<int:pk>', Book.as_view(), name='book'),
    path('create-book/', CreateBook.as_view(), name='create-book'),
]