from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from .models import BookREST
from .serializers import BookSerlaizer


class BookList(APIView):
    """
    Listing all the books stored in the database or adding a new one
    """
    def get(self, request, format=None):
        """
        Get all the readings from the database
        Serialise them (as they're objects) and return the response

        :return: Data for the book with the ID being passed
        """
        readings = BookREST.objects.all()
        serializer = BookSerlaizer(readings, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Take the data that's been sent and de-serialise it before saving

        :return: Status code 201 if a new book was created or shows error 400 if it failed
        """
        serializer = BookSerlaizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetail(APIView):
    """
    Getting individual books by their ID
    Can also update or delete them
    """
    def get_book(self, pk):
        """
        Checking if it is a valid request

        :param pk: ID of the book that is being checked
        :return: Book object or raises an error if the book isn't found in the database
        """
        try:
            return BookREST.objects.get(pk=pk)
        except BookREST.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Getting information for a specified book with its ID

        :param pk: ID of the book
        :return: Data for the Book
        """
        book = self.get_book(pk)
        serializer = BookSerlaizer(book)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        Updating a book on the database with the given ID

        :param pk: ID of the book
        :return: Displays the updated book or shows error 400 if it failed
        """
        book = self.get_book(pk)
        serializer = BookSerlaizer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Deleting a book in the database with the given ID

        :param pk: ID of the book
        :return: Status code 204 after the book has been deleted from the database
        """
        book = self.get_book(pk)
        book.delete()
        return Response(status.HTTP_204_NO_CONTENT)
