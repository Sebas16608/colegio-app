from django.urls import path
from .views import LoginView, RegisterView, UserView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("user", UserView.as_view(), name="user"),
    path("user/<int:pk>/", UserView.as_view(), name="User-detail")
]