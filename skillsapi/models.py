from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Skill(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=360)

class SubSkill(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=360)
    skills = models.ForeignKey(Skill, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

