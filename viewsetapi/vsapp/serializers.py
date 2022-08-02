from rest_framework import serializers
from vsapp.models import User
class UserSerializer(serializers.Serializer):
    user_name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    city = serializers.CharField(max_length=50)

    def create(self, validate_data):
        return User.objects.create(**validate_data)


