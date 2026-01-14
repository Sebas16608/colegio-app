from django.urls import path
from .views import GradeView

urlpatterns = [
    path("grade/", GradeView.as_view(), name="grade-list"),
    path("grade/<int:pk>/", GradeView.as_view(), name="grade-detail")
]