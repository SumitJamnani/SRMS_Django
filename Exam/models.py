from django.contrib.auth.models import User
from django.db import models
from Batch.models import Batch_m
from Course.models import Course_m
from Semester.models import Semester_m
from Subject.models import Subject_m

# Create your models here.

class Exam_m(models.Model):
    exam_id = models.AutoField(primary_key=True)
    exam_name = models.CharField(max_length=30, unique=True)
    batch_id = models.ForeignKey(Batch_m, to_field='batch_id', on_delete=models.CASCADE, db_column='batch_id')
    course_id = models.ForeignKey(Course_m, to_field='course_id', on_delete=models.CASCADE, db_column='course_id')
    semester_id = models.ForeignKey(Semester_m, to_field='semester_id', on_delete=models.CASCADE, db_column='semester_id')
    subject_id = models.ForeignKey(Subject_m, to_field='subject_id', on_delete=models.CASCADE, db_column='subject_id')
    faculty_id = models.ForeignKey(User,on_delete = models.CASCADE, db_column='faculty_id')
    total_marks = models.DecimalField(max_digits=3, decimal_places=0)
    passing_marks = models.DecimalField(max_digits=3, decimal_places=0)
    exam_date = models.DateField()

    def __str__(self):
        return self.exam_name

    class Meta:
        db_table = 'exam_m'
