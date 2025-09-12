from rest_framework.urls import path
from .views import LoginView, CookieJWTRefresh, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('refresh/', CookieJWTRefresh.as_view(), name='refresh'),
    path('logout/', LogoutView.as_view(), name='logout')
]