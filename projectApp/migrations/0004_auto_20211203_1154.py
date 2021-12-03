# Generated by Django 3.2.9 on 2021-12-03 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0003_projects_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='tag',
            field=models.CharField(choices=[('tag1', 'TAG1'), ('tag2', 'TAG2'), ('tag3', 'TAG3'), ('tag4', 'TAG4'), ('tag5', 'TAG5')], default='tag1', max_length=6),
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
    ]
