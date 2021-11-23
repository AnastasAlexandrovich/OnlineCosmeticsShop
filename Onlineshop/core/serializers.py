from rest_framework import serializers

from core.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'second_name', 'avatar']
