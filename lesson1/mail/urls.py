from django.urls import path
from . import views

urlpatterns = [
    path('', views.data),
    path('new', views.test),
]