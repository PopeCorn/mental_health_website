from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('challenges/', views.challenges),
    path('quotes/', views.quotes)
]