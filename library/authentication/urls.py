# # authentication/urls.py
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('register/', views.register, name='register'),
#     path('login/', views.login_view, name='login'),
#     path('logout/', views.logout_view, name='logout'),
#     path('home/', views.home, name='home'),
#     path('users/', views.user_list, name='user_list'),
#     path('user/<int:user_id>/', views.user_detail, name='user_detail'),
#     path('user/<int:user_id>/delete/', views.delete_user, name='delete_user'),  # Шлях для видалення користувачів
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('users/', views.user_list, name='user_list'),
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
    path('users/<int:user_id>/delete/', views.delete_user, name='delete_user'),
]


