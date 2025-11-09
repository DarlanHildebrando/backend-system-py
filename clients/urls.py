from django.urls import path
from .views import RegisterClientView, ClientProfileView, ClientTicketsView

urlpatterns = [
    path('register/', RegisterClientView.as_view(), name='crud-client'),
    path('profile/', ClientProfileView.as_view(), name='client-profile'),
    path('tickets/<uuid:pk>/', ClientTicketsView.as_view(), name='client-tickets')
]