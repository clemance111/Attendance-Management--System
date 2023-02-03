from rest_framework.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import path
from course.views import StudentAPI,CourseAPI,StudentViewset,AttendanceViewSet
router=DefaultRouter()
router.register('students',StudentViewset)
router.register('attendance',AttendanceViewSet)
urlpatterns = [
    # path('',CourseAPI.as_view(),name='course'),
]+router.urls