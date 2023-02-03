from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from students.serializers import StudentSerializer
from students.models import Student
from course.serializers import CourseSerializer,AttendanceSerializer
from course.models import Course,Attendance
from course.impushya import IsTeacher
# Create your views here.


class StudentAPI(APIView):
    # Retrieve
    def get(self, request):
        # query = Student.objects.all()
        # serializer = StudentSerializer(query, many=True)
        return Response({"name":"Lisa"}, status=200)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


# CRUD
class StudentViewset(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    permission_classes=[IsAuthenticated,IsTeacher]

class AttendanceViewSet(viewsets.ModelViewSet):
    serializer_class=AttendanceSerializer
    queryset=Attendance.objects.all()
class CourseAPI(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        query = Course.objects.all()
        serializer = CourseSerializer(query, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)