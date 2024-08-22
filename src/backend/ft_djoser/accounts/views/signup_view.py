from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from typing import Any
from ..serializers.signup_serializer import SignupSerializer

class SignupView(APIView):

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "ユーザーが正常に作成されました"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)