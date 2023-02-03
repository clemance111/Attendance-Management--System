from django.urls import path
from students.views import StudentAPI
urlpatterns = [
    path('',StudentAPI.as_view(),name='students'),   
]