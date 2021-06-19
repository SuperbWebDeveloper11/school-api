from rest_framework import serializers
from .models import Major, Student, Subject, Teacher, Class



class SubjectSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Subject
        fields = ['id', 'name', 'created_by'] 


class ClassSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Class
        fields = ['id', 'name', 'created_by'] 


class MajorSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Major
        fields = ['id', 'name', 'subjects', 'created_by'] 


class StudentSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Student
        fields = ['id', 'username', 'email', 'major', 'created_by'] 

class TeacherSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Teacher
        fields = ['id', 'username', 'email', 'subjects', 'classes', 'created_by'] 


