# Generated by Django 4.1.3 on 2023-02-24 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0005_rename_user_users'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='users',
            new_name='student',
        ),
    ]