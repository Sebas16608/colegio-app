from django.urls import path
from .views import SubmissionView

urlpatterns = [
    path("submission/", SubmissionView.as_view(), name = "submission-list"),
    path("submission/<int:pk>/", SubmissionView.as_view(), name="submission-detail")
]