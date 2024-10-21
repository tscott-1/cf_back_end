from django.db import models
from django.contrib.auth import get_user_model

 # Create your models here.
class Project(models.Model):
    class ProjType(models.TextChoices):
        INDIVIDUAL = "I","Individual"
        RESCUE =  "R","Rescue"
        COMMUNITY =  "C","Community"
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    project_type = models.TextField(choices=ProjType)
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owned_projects'
    )


class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='pledges'
    )
