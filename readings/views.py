from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Reading


class ReadingList(ListView):
    # looks for reading_list.html
    model = Reading
    context_object_name = 'reading_list'


class Book(DetailView):
    # looks for reading_detail.html
    model = Reading
    context_object_name = 'book'

    # will  now look for books.html
    template_name = 'readings/book.html'


class CreateBook(CreateView):
    # looks for reading_form.html
    # will use the models that have been created, and makes a form based on those models and their fields
    model = Reading
    fields = '__all__'
    success_url = reverse_lazy('reading-list')


