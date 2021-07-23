from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Course_m(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=30, unique=True)
    director_id = models.ForeignKey(User,on_delete = models.CASCADE, db_column='director_id', blank=True, null=True)

    def __str__(self):
        return self.course_name

    class Meta:
        db_table = 'course_m'

