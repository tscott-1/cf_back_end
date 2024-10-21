# Generated by Django 5.1 on 2024-10-21 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_pledge_supporter_project_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_type',
            field=models.TextField(choices=[('I', 'Individual'), ('R', 'Rescue'), ('C', 'Community')]),
        ),
    ]
