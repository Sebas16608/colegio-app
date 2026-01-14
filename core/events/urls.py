from django.urls import path
from .views import EventView

urlpatterns = [
    path("events/", EventView.as_view(), name="event-list"),
    path("events/<int:pk>/", EventView.as_view(), name="event-detail")
]