# Generated by Django 4.1.3 on 2023-02-25 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0013_remove_student_marks_delete_mark'),
    ]

    operations = [
        migrations.DeleteModel(
            name='student',
        ),
    ]
