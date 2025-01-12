from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from book.models import Book
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.decorators import login_required

@login_required
def order_list_view(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

@login_required
def order_detail_view(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'order_detail.html', {'order': order})

@login_required
def order_create_view(request):
    if request.method == 'POST':
        book_id = request.POST['book_id']
        book = get_object_or_404(Book, pk=book_id)
        plated_end_at = timezone.now() + timedelta(weeks=2)
        order = Order.objects.create(user=request.user, book=book, plated_end_at=plated_end_at)
        order.save()
        return redirect('order_list')
    books = Book.objects.all()
    return render(request, 'order_form.html', {'books': books})

@login_required
def order_update_view(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.plated_end_at = request.POST['plated_end_at']
        order.end_at = request.POST['end_at']
        order.save()
        return redirect('order_detail', pk=order.pk)
    return render(request, 'order_form.html', {'order': order})

@login_required
def order_delete_view(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'order_confirm_delete.html', {'order': order})

@login_required
def my_orders_view(request):
    user_orders = Order.objects.filter(user=request.user)
    return render(request, 'my_orders.html', {'orders': user_orders})

@login_required
def add_to_order_view(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    plated_end_at = timezone.now() + timedelta(weeks=2)
    order = Order.objects.create(user=request.user, book=book, plated_end_at=plated_end_at)
    order.save()
    return redirect('my_orders')

@login_required
def remove_from_order_view(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if order.user == request.user:
        order.delete()
    return redirect('my_orders')
