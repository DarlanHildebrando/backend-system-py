from django.urls import path
from .views import RegisterClientView, ClientProfileView

urlpatterns = [
    path('register/', RegisterClientView.as_view(), name='crud-client'),
    path('profile/', ClientProfileView.as_view(), name='client-profile')
]