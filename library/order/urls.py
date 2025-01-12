from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list_view, name='order_list'),
    path('<int:pk>/', views.order_detail_view, name='order_detail'),
    path('add/', views.order_create_view, name='order_create'),
    path('<int:pk>/edit/', views.order_update_view, name='order_update'),
    path('<int:pk>/delete/', views.order_delete_view, name='order_delete'),
    path('my_orders/', views.my_orders_view, name='my_orders'),
    path('add_to_order/<int:book_id>/', views.add_to_order_view, name='add_to_order'),
    path('remove_from_order/<int:order_id>/', views.remove_from_order_view, name='remove_from_order'),
]
