from rest_framework import serializers

from api.models import User


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    birth_of_date = serializers.DateField()
    tel = serializers.CharField()

    class Meta:
        model = User
        fields = [
            "avatar",
            "first_name",
            "last_name",
            "email",
            "password",
            "birth_of_date",
            "tel",
        ]
