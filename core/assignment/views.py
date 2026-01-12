from django.shortcuts import render
from API import SuperApiView
from .models import Assignment
from .serializers import AssigmentSerializer
# Create your views here.
class AssignmentView(SuperApiView):
    model = Assignment
    serializer_class = AssigmentSerializer
    filter_fields = ["title"]