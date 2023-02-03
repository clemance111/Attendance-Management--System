from django.db import models
from django.db import models
from students.models import Student
# Create your models here.


class Course(models.Model):
    course_code = models.CharField(max_length=5)
    course_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.course_name} {self.course_code}"


class CourseStudents(models.Model):
    course = models.ForeignKey(
        Course, related_name='course_students', on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name='courses')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course.course_name

class Attendance(models.Model):
    ABSENT="A"
    PRESENT="P"
    PERMISSION="PM"

    ATTENDANCE_STATUS=(
        (ABSENT,"Yasibye"),
        (PRESENT,"yatabiriye"),
        (PERMISSION,"Afite uruhushya")
    )
    course=models.ForeignKey(Course,related_name='attendances',on_delete=models.CASCADE)
    student=models.ForeignKey(Student,related_name='student_attendance',on_delete=models.CASCADE)
    attendance_status=models.CharField(choices=ATTENDANCE_STATUS,max_length=2,default=PERMISSION)  
    attended_on=models.DateField()    
    recorded_on=models.DateTimeField(auto_now_add=True)  