from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "password", "email"]

    def create(self, validate_data):
        user = User(
            username = validate_data["username"],
            email = validate_data["email"],
            first_name = validate_data["first_name"],
            last_name = validate_data["last_name"],
        )
        user.set_password(validate_data["password"])
        user.save()
        return user