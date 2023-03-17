from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.urls import reverse_lazy
from .models import Reading


class ReadingList(LoginRequiredMixin, ListView):
    """
    Displays all the books that the user has stored on the database
    The template separates currently reading books from books that have not been started
    Looks for reading_list.html by default
    """
    model = Reading
    context_object_name = 'reading_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reading_list'] = context['reading_list'].filter(user=self.request.user)

        # allowing the user to search for books
        user_input = self.request.GET.get('search-box')
        if user_input:
            context['reading_list'] = context['reading_list'].filter(title__icontains=user_input)
        context['user_input'] = user_input

        return context


class Book(LoginRequiredMixin, DetailView):
    """
    Displays information about books in a separate page
    Passes the ID to be able to view them
    Looks for reading_detail.html by default
    """
    model = Reading
    context_object_name = 'book'

    # will  now look for books.html
    template_name = 'readings/book.html'


class CreateBook(LoginRequiredMixin, CreateView):
    """
    Generates a form where the user can add new books onto the database - only asks for a few user inputs
    Will use the models that has been created, and makes a form based on those models and their fields
    Error messages shown by Django's built-in methods
    Looks for reading_form.html by default
    """
    model = Reading
    fields = ['title', 'author', 'genre', 'pages', 'started_reading', 'current_page']
    success_url = reverse_lazy('reading-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateBook, self).form_valid(form)


class UpdateBook(LoginRequiredMixin, UpdateView):
    """
    Displays a form filled with data for the selected book - all the fields are shown except username
    Will use the model that has been created, and makes a form based on those models and their fields
    Error messages shown by Django's built-in methods
    Looks for reading_form.html by default
    """
    model = Reading
    fields = ['title', 'author', 'genre', 'pages', 'started_reading', 'current_page', 'finished_reading',
              'thoughts', 'summary', 'recommended']
    success_url = reverse_lazy('reading-list')


class DeleteBook(LoginRequiredMixin, DeleteView):
    """
    Deletes the selected book - asks to confirm before deleting
    Looks for reading_confirm_delete.html by default
    """
    model = Reading
    context_object_name = 'book'
    success_url = reverse_lazy('reading-list')


class UserLogin(LoginView):
    """
    User login form - redirects to the readings-list view once successful
    Error messages shown by Django's built-in methods
    Logging out is done directly from views.py
    """
    template_name = 'readings/login.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('reading-list')


class RegisterUser(FormView):
    """
    Allows for new users to sign up
    Shows default Django requirements for username and password
    """
    template_name = 'readings/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('reading-list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterUser, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('reading-list')
        return super(RegisterUser, self).get(*args, **kwargs)
