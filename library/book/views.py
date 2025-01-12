from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from author.models import Author
from django.contrib.auth.decorators import user_passes_test

def book_list_view(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})

# @user_passes_test(lambda u: u.is_superuser)
def book_create_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        count = request.POST['count']
        author_ids = request.POST.getlist('authors')
        if not author_ids:
            return render(request, 'book_form.html', {'error': 'Please select at least one author.', 'authors': Author.objects.all()})
        book = Book.objects.create(name=name, description=description, count=count)
        book.save()
        for author_id in author_ids:
            author = Author.objects.get(pk=author_id)
            book.authors.add(author)
        return redirect('book_list')
    authors = Author.objects.all()
    return render(request, 'book_form.html', {'authors': authors})

# @user_passes_test(lambda u: u.is_superuser)
def book_update_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.name = request.POST['name']
        book.description = request.POST['description']
        book.count = request.POST['count']
        author_ids = request.POST.getlist('authors')
        if not author_ids:
            return render(request, 'book_form.html', {'error': 'Please select at least one author.', 'authors': Author.objects.all(), 'book': book})
        book.save()
        book.authors.clear()
        for author_id in author_ids:
            author = Author.objects.get(pk=author_id)
            book.authors.add(author)
        return redirect('book_detail', pk=book.pk)
    authors = Author.objects.all()
    return render(request, 'book_form.html', {'book': book, 'authors': authors})

# @user_passes_test(lambda u: u.is_superuser)
def book_delete_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book_confirm_delete.html', {'book': book})
