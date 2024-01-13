from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('cost_table/', cost_table, name='cost_table'),
]
