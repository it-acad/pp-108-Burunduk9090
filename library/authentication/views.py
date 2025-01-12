from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.http import HttpResponse

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'user_list.html', {'users': users})

@login_required
def user_detail(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'role': user.get_role_name(),
    }
    if request.user.role == 1 or request.user == user:
        context.update({
            'middle_name': user.middle_name,
            'created_at': user.created_at,
            'updated_at': user.updated_at,
            'is_active': user.is_active,
        })
    return render(request, 'user_detail.html', {'user': user, 'context': context})

@login_required
def delete_user(request, user_id):
    if request.user.role == 1:
        user = get_object_or_404(CustomUser, id=user_id)
        if user.role != 1 and user != request.user:
            user.delete()
    return redirect('user_list')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        middle_name = request.POST['middle_name']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST.get('role', 0)
        user = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, middle_name=middle_name, email=email, password=password, role=role)
        user.save()
        login(request, user)
        return redirect('home')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Invalid login details")
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
