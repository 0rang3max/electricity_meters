
from django.urls import path

from . import views

urlpatterns = [
    path('', views.items_list, name='index'),
    path('<int:pk>/', views.item_detail, name='detail'),
]
