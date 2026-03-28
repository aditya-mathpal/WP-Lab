from django.shortcuts import render, redirect
from .models import Author, Publisher, Book
from .forms import AuthorForm, PublisherForm, BookForm


def index(request):
    books = Book.objects.all()

    return render(request, 'index.html', {
        'books': books
    })


def add_author(request):
    form = AuthorForm()

    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/library/')

    return render(request, 'add_author.html', {'form': form})


def add_publisher(request):
    form = PublisherForm()

    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/library/')

    return render(request, 'add_publisher.html', {'form': form})


def add_book(request):
    form = BookForm()

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/library/')

    return render(request, 'add_book.html', {'form': form})