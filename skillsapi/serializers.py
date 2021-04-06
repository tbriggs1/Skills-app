from rest_framework import serializers
from .models import Skill, SubSkill

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('id', 'title', 'subSkill', 'employee_rating', 'manager_rating', 'studID')


class SubSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubSkill
        fields = ('id', 'title')


