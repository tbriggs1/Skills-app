from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator




class Skill(models.Model):
    title = models.CharField(max_length=32, default="Add Skill")
    employee_rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    manager_rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    studID = models.CharField(max_length=32, default="default_user")

# class SubSkill(models.Model):
#     title = models.CharField(max_length=32)
#
#     employee_rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
#     manager_rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)


class AdditionalSkill(models.Model):
    title = models.CharField(max_length=32, default="Add Skill")
    comments = models.CharField(max_length=108, default="comments")
    acquired = models.CharField(max_length=32, default="twat")
    employee_rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    manager_rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    studID = models.CharField(max_length=32, default="default_user")

# class EssentialSkill(models.Model):
#     title = models.CharField(max_length=32, default="Add Skill")
#     employee_rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
#     manager_rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
#     studID = models.CharField(max_length=32, default="default_user")
#
#
