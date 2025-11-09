from django.urls import path
from .views import AccessibilityEventsView

urlpatterns = [
    path('accessibility/<uuid:pk>', AccessibilityEventsView.as_view(), name='accessibility-events')
]