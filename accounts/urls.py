from django.urls import path
from .views import CustomerListCreateView, CustomerRetriveUpdateDeleteView


urlpatterns = [
    path('customers/', CustomerListCreateView.as_view(),name='customer-list-create'),
    path('customers/<int:pk>/', CustomerRetriveUpdateDeleteView.as_view(),name='customer_detail'),
]