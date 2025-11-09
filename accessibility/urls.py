from django.urls import path
from .views import VisualConfigurationView

urlpatterns = [
    path('registerConfig/', VisualConfigurationView.as_view(), name='register-config')
]