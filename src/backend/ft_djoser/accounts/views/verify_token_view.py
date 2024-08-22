from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import jwt
from jwt import ExpiredSignatureError, InvalidTokenError
from django.conf import settings

from rest_framework.request import Request
from typing import Any, Dict

class VerifyTokenView(APIView):
    def post(self, request: Request, *args: Any, **kwargs: Any):
        token: str = request.data.get('access_token')

        if not token:
            return Response({"detail": "トークンが提供されていません。"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # トークンをデコードして検証
            decoded_token:str = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            return Response({"detail": "トークンは有効です。"}, status=status.HTTP_200_OK)

        except ExpiredSignatureError:
            # トークンが期限切れの場合
            return Response({"detail": "トークンの有効期限が切れています。"}, status=status.HTTP_401_UNAUTHORIZED)
        except InvalidTokenError:
            # トークンが無効な場合
            return Response({"detail": "無効なトークンです。"}, status=status.HTTP_401_UNAUTHORIZED)