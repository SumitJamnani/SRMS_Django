from django.db import models
from Course.models import Course_m
from Semester.models import Semester_m

# Create your models here.

class Batch_m(models.Model):
    batch_id = models.AutoField(primary_key=True)
    batch_name = models.CharField(max_length=30, unique=True)
    course_id = models.ForeignKey(Course_m, to_field='course_id', on_delete=models.CASCADE, db_column='course_id')
    semester_id = models.ForeignKey(Semester_m, to_field='semester_id', on_delete=models.CASCADE, db_column='semester_id')

    def __str__(self):
        return self.batch_name

    class Meta:
        db_table = 'batch_m'
