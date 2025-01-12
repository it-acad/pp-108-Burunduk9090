from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.author_list_view, name='author_list'),
    path('authors/<int:pk>/', views.author_detail_view, name='author_detail'),
    path('authors/add/', views.author_create_view, name='author_create'),
    path('authors/<int:pk>/edit/', views.author_update_view, name='author_update'),
    path('authors/<int:pk>/delete/', views.author_delete_view, name='author_delete'),
]
