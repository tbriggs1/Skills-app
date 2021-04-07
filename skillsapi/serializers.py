from rest_framework import serializers
from .models import Skill,  AdditionalSkill

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('id', 'title', 'employee_rating', 'manager_rating', 'studID')

# class SubSkillSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SubSkill
#         fields = ('id', 'title', 'employee_rating', 'manager_rating', 'studID' )


class AdditionalSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalSkill
        fields = ('id', 'title', 'comments', 'employee_rating', 'manager_rating', 'studID')

# class EssentialSkillSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Skill
#         fields = ('id', 'title', 'employee_rating', 'manager_rating', 'studID')