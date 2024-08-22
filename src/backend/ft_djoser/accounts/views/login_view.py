from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from typing import Any, Dict

from ..serializers.login_serializer import LoginSerializer

import jwt
import datetime
from django.conf import settings

class LoginView(APIView):

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']

            # 現在のUTC時刻を取得
            current_time = datetime.datetime.now(datetime.timezone.utc)

            # トークンのペイロード設定
            access_token_payload: Dict[str, Any] = {
                'user_id': user.id,
                'exp': current_time + datetime.timedelta(minutes=5),  # 有効期限5分
                'iat': current_time,  # 発行時間
            }
            
            refresh_token_payload: Dict[str, Any] = {
                'user_id': user.id,
                'exp': current_time + datetime.timedelta(days=7),  # 有効期限7日
                'iat': current_time,
            }

            # トークンの生成
            access_token: str = jwt.encode(access_token_payload, settings.SECRET_KEY, algorithm='HS256')
            refresh_token: str = jwt.encode(refresh_token_payload, settings.SECRET_KEY, algorithm='HS256')

            #refresh = RefreshToken.for_user(user)
            return Response({
                'access_token': access_token,
                'refresh_token': refresh_token,
                'user_id': user.id,
                'email': user.email
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)