from django.urls import path
from .views import CrudClient

urlpatterns = [
    path('client/', CrudClient.as_view(), name='crud-client')
]