from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class SubSkill(models.Model):
    title = models.CharField(max_length=32)


class Skill(models.Model):
    title = models.CharField(max_length=32, default="Add Skill")
    subSkill = models.ForeignKey(SubSkill, max_length=32, default="N/A", on_delete=models.CASCADE)
    employee_rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    manager_rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    studID = models.CharField(max_length=32, default="default_user")



