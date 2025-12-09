from django.urls import path
from .views import AccessibilityEventsView, ReturnEventView

urlpatterns = [
    path('accessibility/<uuid:pk>', AccessibilityEventsView.as_view(), name='accessibility-events'),
    path('event/<str:id>/', ReturnEventView.as_view(), name='get-event')
]