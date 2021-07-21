# Generated by Django 3.2.3 on 2021-07-19 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Course', '0001_initial'),
        ('Batch', '0001_initial'),
        ('Semester', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject_m',
            fields=[
                ('subject_id', models.AutoField(primary_key=True, serialize=False)),
                ('subject_name', models.CharField(max_length=30, unique=True)),
                ('subject_type', models.CharField(max_length=30, unique=True)),
                ('batch_id', models.ForeignKey(db_column='batch_id', on_delete=django.db.models.deletion.CASCADE, to='Batch.batch_m')),
                ('course_id', models.ForeignKey(db_column='course_id', on_delete=django.db.models.deletion.CASCADE, to='Course.course_m')),
                ('semester_id', models.ForeignKey(db_column='semester_id', on_delete=django.db.models.deletion.CASCADE, to='Semester.semester_m')),
            ],
            options={
                'db_table': 'subject_m',
            },
        ),
    ]
