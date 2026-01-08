from rest_framework import serializers
from .models import Assignment

class AssigmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = "__all__"