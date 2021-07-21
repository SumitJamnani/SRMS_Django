# Generated by Django 3.2.3 on 2021-07-19 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester_m',
            fields=[
                ('semester_id', models.AutoField(primary_key=True, serialize=False)),
                ('semester_name', models.CharField(max_length=30, unique=True)),
                ('course_id', models.ForeignKey(db_column='course_id', on_delete=django.db.models.deletion.CASCADE, to='Course.course_m')),
            ],
            options={
                'db_table': 'semester_m',
            },
        ),
    ]