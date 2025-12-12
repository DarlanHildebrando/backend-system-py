from django.urls import path
from .views import ProductView

urlpatterns = [
    path('product/', ProductView.as_view(), name='crud-product'),
    path('update-sale/<uuid:pk>/', ProductView.as_view(), name='update-sale'),

    # path('trackOrder/')
]