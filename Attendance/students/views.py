from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from students.serializers import StudentSerializer
from students.models import Student
# Create your views here.


class StudentAPI(APIView):
    def get(self, request):
        query = Student.objects.all()
        serializer = StudentSerializer(query, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)