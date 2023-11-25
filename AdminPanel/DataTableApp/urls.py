from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index),
    path('cost_table/', cost_table, name='cost_table'),
]