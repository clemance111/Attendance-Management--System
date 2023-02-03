from rest_framework import serializers
from course.models import CourseStudents, Course,Attendance
from django.utils import timezone

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attendance
        fields='__all__'
    def validate(self, attrs):
        student=attrs['student']
        course=attrs['course']
        date=attrs['attended_on']
        if Attendance.objects.filter(student=student,course=course,attended_on=date).exists():
            raise serializers.ValidationError({"attendance_error":"Twamaze kruikodinga"})
        return super().validate(attrs)
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


    def validate_course_code(self, value):
        if Course.objects.filter(course_code=value).exists():
            raise serializers.ValidationError(
                "Course with coede already  exist")
        else:
            return value
        # try:
        #     Course.objects.get(course_code=value)
        #     raise serializers.ValidationError("something")
        # except Course.DoesNotExist:
        #     return value


class CourseStudentsSerializer(serializers.ModelSerializer):
    current_time = serializers.DateTimeField(default=timezone.now())

    class Meta:
        model = CourseStudents
        fields = [
            'id',
            'course',
            'students',
            'current_time'
        ]