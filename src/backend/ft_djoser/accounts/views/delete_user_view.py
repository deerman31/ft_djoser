from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class DeleteUserView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        # 認証されたユーザーを取得
        user = request.user

        # ユーザーを削除
        user.delete()
        return Response({"message": "ユーザーが正常に削除されました"}, status=status.HTTP_204_NO_CONTENT)