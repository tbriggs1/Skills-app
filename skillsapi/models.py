from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Skill(models.Model):
    title = models.CharField(max_length=32, default="Add Skill")
    subSkill = models.CharField(max_length=32, default="Add Second Skill")
    employee_rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    manager_rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    studID = models.CharField(max_length=32, default="default_user")

class SubSkill(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=360)
    skills = models.ForeignKey(Skill, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

