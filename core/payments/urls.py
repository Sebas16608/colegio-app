from django.urls import path
from .views import PaymentView

urlpatterns = [
    path("payments/", PaymentView.as_view(), name = "payments-list-filter"),
    path("payments/<int:pk>/", PaymentView.as_view(), name="payment-detail")
]