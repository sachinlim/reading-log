from rest_framework import serializers

from .models import BookREST


class BookSerlaizer(serializers.ModelSerializer):
    class Meta:
        model = BookREST
        fields = ['id', 'title', 'author', 'genre', 'pages']
