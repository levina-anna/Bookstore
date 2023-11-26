from django.contrib import admin
from DataTableApp.views import *
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('DataTableApp.urls')),
]
