from rest_framework.views import APIView
from users.serializers import UserCreateSerializer
from rest_framework.response import Response


class UserAPI(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)