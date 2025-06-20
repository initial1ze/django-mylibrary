from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Book
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Book

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books/book_list.html'

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)

class BookDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Book
    template_name = 'books/book_detail.html'

    def test_func(self):
        return self.get_object().user == self.request.user

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'publication_year', 'isbn']
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'publication_year', 'isbn']
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book-list')

    def test_func(self):
        return self.get_object().user == self.request.user

class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('book-list')

    def test_func(self):
        return self.get_object().user == self.request.user


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created! You can now log in.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'books/register.html', {'form': form})
