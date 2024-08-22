from rest_framework import serializers
#from django.contrib.auth import get_user_model

#User = get_user_model()
from ..models import UserAccount

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    re_password = serializers.CharField(write_only=True)

    class Meta:
        model = UserAccount
        fields = ['name', 'email', 'password', 're_password']
    
    def validate_name(self, value):
        if UserAccount.objects.filter(name=value).exists():
            raise serializers.ValidationError("この名前は既に使用されています。")
        return value
    def validate_email(self, value):
        if UserAccount.objects.filter(email=value).exists():
            raise serializers.ValidationError("このメールアドレスは既に使用されています。")
        return value

    def validate(self, data):
        if data['password'] != data['re_password']:
            raise serializers.ValidationError("パスワードが一致しません。")
        return data


    def create(self, validated_data):
        validated_data.pop('re_password')
        user = UserAccount.objects.create_user(
            name=validated_data['name'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user