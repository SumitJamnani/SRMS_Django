from django.db import models
from Course.models import Course_m

# Create your models here.

class Semester_m(models.Model):
    semester_id = models.AutoField(primary_key=True)
    semester_name = models.CharField(max_length=30)
    course_id = models.ForeignKey(Course_m, to_field='course_id', on_delete=models.CASCADE, db_column='course_id')

    def __str__(self):
        return self.semester_name

    class Meta:
        db_table = 'semester_m'
