from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
User=get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
    def validate_password(self,password_str):
        try:
            validate_password(password_str)
            return password_str
        except Exception as e:
            raise serializers.ValidationError(e)
    def create(self, validated_data):
        user=super().create(validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user
        