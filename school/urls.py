from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [

    # ****************** subject urls ****************** 
    path('subject/', views.SubjectList.as_view()),
    path('subject/<int:pk>/', views.SubjectDetail.as_view()),


    # ****************** class urls ****************** 
    path('class/', views.ClassList.as_view()),
    path('class/<int:pk>/', views.ClassDetail.as_view()),

    # ****************** major urls ****************** 
    path('major/', views.MajorList.as_view()),
    path('major/<int:pk>/', views.MajorDetail.as_view()),

    # ****************** student urls ****************** 
    path('student/', views.StudentList.as_view()),
    path('student/<int:pk>/', views.StudentDetail.as_view()),

    # ****************** teacher urls ****************** 
    path('teacher/', views.TeacherList.as_view()),
    path('teacher/<int:pk>/', views.TeacherDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

