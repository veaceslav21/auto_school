from .models import Account
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password


class AccountSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Account
        fields = ['id', 'email', 'password', 'password2', 'first_name', 'last_name', 'driver']
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'driver': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': 'Password did not match'})
        return attrs

    def create(self, validated_data):
        account = Account.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            driver=validated_data['driver']
        )
        account.set_password(validated_data['password'])
        account.save()
        return account