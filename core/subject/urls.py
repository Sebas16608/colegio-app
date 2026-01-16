from django.urls import path
from .views import SubjectView

urlpatterns = [
    path("subjects/", SubjectView.as_view(), name="subjects-list-filter"),
    path("subjects/<int:pk>/", SubjectView.as_view(), name="subjects-detail")
]