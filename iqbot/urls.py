from . import views
from django.urls import path

urlpatterns = [
    path('', views.landing, name='landing'),
    path('home/', views.home, name='home'),
]