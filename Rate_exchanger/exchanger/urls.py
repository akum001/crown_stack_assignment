from django.urls import path
from .views import index, exchange_rate_calculator

urlpatterns = [
    path('', index),
    path('calculate_exchange', exchange_rate_calculator )
]
