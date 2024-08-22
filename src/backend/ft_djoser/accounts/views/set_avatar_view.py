from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..serializers.avatar_serializer import AvatarSerializer

class SetAvatarView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        serializer = AvatarSerializer(user, data=request.data, partial=True)  # partial=Trueを追加

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "アバターが正常にアップロードされました"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)