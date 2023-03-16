from django.db import models
from django.contrib.auth.models import User


class Reading(models.Model):
    # if a user is deleted, their logs are deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    pages = models.CharField(max_length=5)
    current_page = models.CharField(max_length=5, null=True, blank=True)

    started_reading = models.DateField(null=True, blank=True)
    finished_reading = models.DateField(null=True, blank=True)

    thoughts = models.TextField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    recommended = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
