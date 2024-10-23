from django.urls import path
from .views import AccountListCreateView, AccountDetailView

urlpatterns = [
    # Contacts URLs
    path('contacts/', AccountListCreateView.as_view(), name='account-list-create'),
    path('contacts/<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
]