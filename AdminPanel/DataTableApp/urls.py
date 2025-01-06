from django.urls import path
from .views import IndexView, CostTableView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cost_table/', CostTableView.as_view(), name='cost_table'),
]
