from django.shortcuts import render, get_object_or_404, redirect
from .models import Author
from django.contrib.auth.decorators import user_passes_test

def author_list_view(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})

def author_detail_view(request, pk):
    author = get_object_or_404(Author, pk=pk)
    books = author.books.all()
    return render(request, 'author_detail.html', {'author': author, 'books': books})

# @user_passes_test(lambda u: u.is_superuser)
def author_create_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        patronymic = request.POST['patronymic']
        author = Author.objects.create(name=name, surname=surname, patronymic=patronymic)
        author.save()
        return redirect('author_list')
    return render(request, 'author_form.html')

# @user_passes_test(lambda u: u.is_superuser)
def author_update_view(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.name = request.POST['name']
        author.surname = request.POST['surname']
        author.patronymic = request.POST['patronymic']
        author.save()
        return redirect('author_detail', pk=author.pk)
    return render(request, 'author_form.html', {'author': author})

# @user_passes_test(lambda u: u.is_superuser)
def author_delete_view(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('author_list')
    return render(request, 'author_confirm_delete.html', {'author': author})
