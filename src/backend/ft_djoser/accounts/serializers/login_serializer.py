from rest_framework import serializers
from django.contrib.auth import authenticate
from ..models import UserAccount
from typing import List, Dict, Any

class LoginSerializer(serializers.Serializer):
    identifier = serializers.CharField()  # nameかemailを受け取る
    password = serializers.CharField(write_only=True)

    def validate(self, data: dict) -> dict:
        identifier: str = data.get('identifier')
        password: str = data.get('password')

        if identifier and password:
            # identifierがemailの形式かどうかをチェック
            if '@' in identifier:
                try:
                    user: UserAccount = UserAccount.objects.get(email__iexact=identifier)
                except UserAccount.DoesNotExist:
                    raise serializers.ValidationError("無効なメールアドレスです。")
            else:
                try:
                    user: UserAccount = UserAccount.objects.get(name__iexact=identifier)
                except UserAccount.DoesNotExist:
                    raise serializers.ValidationError("無効な名前です。")

            # 認証をemailで行う
            user = authenticate(request=self.context.get('request'), email=user.email, password=password)

            if user is None:
                raise serializers.ValidationError("メールアドレスまたはパスワードが正しくありません。")
            if not user.is_active:
                raise serializers.ValidationError("このアカウントは無効です。")
        else:
            raise serializers.ValidationError("メールアドレス/名前とパスワードは必須です。")

        data['user'] = user
        return data