# Generated by Django 5.1 on 2024-09-17 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_remove_project_project_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_type',
            field=models.TextField(choices=[], default='Individual'),
            preserve_default=False,
        ),
    ]