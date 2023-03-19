from django.db import models


class BookREST(models.Model):
    """
    Similar model as the one for the main project
    Using this model to learn about REST APIs with Django
    """
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    pages = models.CharField(max_length=5)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
