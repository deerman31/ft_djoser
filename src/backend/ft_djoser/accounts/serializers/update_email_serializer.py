from rest_framework import serializers
from ..models import UserAccount

class UpdateEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['email']

    def validate_email(self, value):
        if UserAccount.objects.filter(email=value).exists():
            raise serializers.ValidationError("このメールアドレスは既に使用されています。")
        return value