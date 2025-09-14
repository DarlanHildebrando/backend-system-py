from django.urls import path
from .views import CrudEnterprise

urlpatterns = [
    path('crud/', CrudEnterprise.as_view(), name="enterprise-crud")
]