from django.db import models
from Batch.models import Batch_m
from Course.models import Course_m
from Semester.models import Semester_m

# Create your models here.

class Subject_m(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=30, unique=True)
    subject_code = models.CharField(max_length=30, default='')
    subject_type = models.CharField(max_length=30)
    course_id = models.ForeignKey(Course_m, to_field='course_id', on_delete=models.CASCADE, db_column='course_id')
    semester_id = models.ForeignKey(Semester_m, to_field='semester_id', on_delete=models.CASCADE, db_column='semester_id')
    batch_id = models.ForeignKey(Batch_m, to_field='batch_id', on_delete=models.CASCADE, db_column='batch_id')

    def __str__(self):
        return self.subject_name

    class Meta:
        db_table = 'subject_m'
