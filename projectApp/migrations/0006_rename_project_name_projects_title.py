# Generated by Django 3.2.9 on 2021-12-03 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0005_auto_20211203_1156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='project_name',
            new_name='title',
        ),
    ]
