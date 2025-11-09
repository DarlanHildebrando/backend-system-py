from django.urls import path
from .views import CrudEnterprise, EnterpriseProfileView

urlpatterns = [
    path('crud/', CrudEnterprise.as_view(), name="enterprise-crud"),
    path('profile/<uuid:pk>',EnterpriseProfileView.as_view(), name="enterprise-profile" )
]