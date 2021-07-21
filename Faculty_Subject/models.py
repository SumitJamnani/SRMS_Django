from django.contrib.auth.models import User
from django.db import models
from django.db import models
from Batch.models import Batch_m
from Course.models import Course_m
from Semester.models import Semester_m
from Subject.models import Subject_m

# Create your models here.

class Faculty_m(models.Model):
    fact_subject_id = models.AutoField(primary_key=True)
    batch_id = models.ForeignKey(Batch_m, to_field='batch_id', on_delete=models.CASCADE, db_column='batch_id')
    course_id = models.ForeignKey(Course_m, to_field='course_id', on_delete=models.CASCADE, db_column='course_id')
    faculty_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='faculty_id')
    semester_id = models.ForeignKey(Semester_m, to_field='semester_id', on_delete=models.CASCADE, db_column='semester_id')
    subject_id = models.ForeignKey(Subject_m, to_field='subject_id', on_delete=models.CASCADE, db_column='subject_id')

    class Meta:
        db_table = 'faculty_subject_m'
