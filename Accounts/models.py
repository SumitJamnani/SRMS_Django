from decimal import Decimal
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class ExtendedUser(models.Model):
    user_role = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, unique=True, error_messages = {"email": "Please Enter Valid Email!!"})
    enrollment_number = models.BigIntegerField(null=True, blank=True, default=0)
    course_name = models.CharField(max_length=30, null=True, blank=True)
    semester_name = models.CharField(max_length=30, null=True, blank=True)
    division_name = models.CharField(max_length=30, null=True, blank=True)
    batch_name = models.CharField(max_length=30, null=True, blank=True)
    elective_subject = models.CharField(max_length=30, null=True, blank=True)
    user = models.OneToOneField(User,on_delete = models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'extendeduser'


