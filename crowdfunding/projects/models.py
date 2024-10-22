from django.db import models
from django.contrib.auth import get_user_model

 # Create your models here.

class SportsList(models.Model): 
    sport = models.TextField()
    sport_type = models.TextField()


class Sportsclub(models.Model):
    size = [
        ("S", "< 10 Members"),
        ("M", "10-50 Members"),
        ("L", "50-120 Members"),
        ("XL", ">120 Members"),
    ]
    club = models.CharField(max_length=200)
    description = models.TextField()
    sport = models.ForeignKey(
        'SportsList',
        on_delete=models.RESTRICT,
        related_name = "clubs"
    )
    club_size = models.TextField(choices=size)
    club_location = models.TextField()
    is_active = models.BooleanField()
    club_logo = models.URLField()
    club_owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='clubs_managed'
    )
    club_members = models.ManyToManyField(
        get_user_model(),
        related_name = "club_membership",
    )


class Project(models.Model):
    FundType = [
        ("E", "Equipment and Uniforms"),
        ("C", "Competitions and Events"),
        ("F", "Players Fees"),
        ("S", "Coaching"),
        ("I", "Club Infrastructure")
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    Fund_type = models.TextField(choices=FundType)
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    member_only = models.BooleanField()
    owner = models.ForeignKey(
        'Sportsclub',
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
