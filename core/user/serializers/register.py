from rest_framework import serializers
from ..models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password"]

        def create(self, validate_data):
            user = User(
                username = validate_data["username"],
                first_name = validate_data["first_name"],
                last_name = validate_data["last_name"],
                email = validate_data["email"],                
            )
            user.set_password(validate_data["password"])
            user.save()
            return user