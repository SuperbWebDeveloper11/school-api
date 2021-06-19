from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, generics
from .serializers import SubjectSerializer, ClassSerializer, MajorSerializer, StudentSerializer, TeacherSerializer
from .models import Subject, Class, Major, Student, Teacher
from .permissions import IsOwnerOrReadOnly

"""
The following views perform crud operations for 5 models:
    - Class
    - Teacher
    - Subject
    - Student
    - Major
"""

# ***************** subject views ***************** 
class SubjectList(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer): # add the subject created_by
        serializer.save(created_by=self.request.user)

class SubjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
                        

# ***************** class views ***************** 
class ClassList(generics.ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer): # add the class created_by
        serializer.save(created_by=self.request.user)

class ClassDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
                        

# ***************** major views ***************** 
class MajorList(generics.ListCreateAPIView):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer): # add the class created_by
        serializer.save(created_by=self.request.user)

class MajorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
                        

# ***************** student views ***************** 
class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer): # add the student created_by
        serializer.save(created_by=self.request.user)

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
                        

# ***************** teacher views ***************** 
class TeacherList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer): # add the teacher created_by
        serializer.save(created_by=self.request.user)

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
                        

