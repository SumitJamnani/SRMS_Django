# Generated by Django 3.2.3 on 2021-07-20 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Subject', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject_m',
            name='subject_code',
            field=models.CharField(default='', max_length=30),
        ),
    ]
