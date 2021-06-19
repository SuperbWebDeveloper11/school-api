from django.db import models


# ***************** abstract model ***************** 
class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now =True)

    class Meta:
        abstract = True
        ordering = ['-created']

    def __str__(self):
        return self.name


# ***************** 5 models created using the TimeStampedModel ***************** 

class Subject(TimeStampedModel):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey('auth.User', related_name="created_subjects", on_delete=models.CASCADE)

class Class(TimeStampedModel):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey('auth.User', related_name="created_classes", on_delete=models.CASCADE)


class Major(TimeStampedModel):
    name = models.CharField(max_length=100)
    subjects = models.ManyToManyField(Subject, related_name="majors")
    created_by = models.ForeignKey('auth.User', related_name="created_majors", on_delete=models.CASCADE)


class Student(TimeStampedModel):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True, null=True)
    major = models.ForeignKey(Major, related_name="students", on_delete=models.CASCADE)
    created_by = models.ForeignKey('auth.User', related_name="created_students", on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class Teacher(TimeStampedModel):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True, null=True)
    subjects = models.ManyToManyField(Major, related_name="subject_teachers")
    classes = models.ManyToManyField(Major, related_name="class_teachers")
    created_by = models.ForeignKey('auth.User', related_name="created_teachers", on_delete=models.CASCADE)

    def __str__(self):
        return self.username




