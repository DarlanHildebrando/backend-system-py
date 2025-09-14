from django.urls import path
from .views import CrudClient

urlpatterns = [
    path('crud/', CrudClient.as_view(), name='crud-client')
]