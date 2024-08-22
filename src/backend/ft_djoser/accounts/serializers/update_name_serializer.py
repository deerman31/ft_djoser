from rest_framework import serializers
from ..models import UserAccount

class UpdateNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['name']

    def validate_email(self, value):
        if UserAccount.objects.filter(name=value).exists():
            raise serializers.ValidationError("この名前は既に使用されています。")
        return value