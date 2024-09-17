from django.db import models

 # Create your models here.
class Project(models.Model):
    class ProjType(models.TextChoices):
        INDIVIDUAL = "Individual"
        RESCUE =  "Rescue"
        COMMUNITY =  "Community"
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    project_type = models.TextField(choices=ProjType)
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
