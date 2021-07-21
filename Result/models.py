from django.contrib.auth.models import User
from django.db import models
from django.db import models
from Batch.models import Batch_m
from Course.models import Course_m
from Exam.models import Exam_m
from Semester.models import Semester_m
from Subject.models import Subject_m

# Create your models here.

class Result_m(models.Model):
    result_id = models.AutoField(primary_key=True)
    exam_id = models.ForeignKey(Exam_m, to_field='exam_id', on_delete=models.CASCADE, db_column='exam_id')
    batch_id = models.ForeignKey(Batch_m, to_field='batch_id', on_delete=models.CASCADE, db_column='batch_id')
    course_id = models.ForeignKey(Course_m, to_field='course_id', on_delete=models.CASCADE, db_column='course_id')
    semester_id = models.ForeignKey(Semester_m, to_field='semester_id', on_delete=models.CASCADE, db_column='semester_id')
    subject_id = models.ForeignKey(Subject_m, to_field='subject_id', on_delete=models.CASCADE, db_column='subject_id')
    faculty_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='faculty_id')
    enrollment_number = models.BigIntegerField(null=True, blank=True, default=0)
    marks_obtained = models.DecimalField(max_digits=3, decimal_places=0)
    status = models.CharField(max_length=30)

    class Meta:
        db_table = 'result_m'
