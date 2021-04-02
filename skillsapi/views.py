from django.shortcuts import render
from rest_framework import viewsets
from .models import Skill, SubSkill
from .serializers import SkillSerializer, SubSkillSerializer

# Create your views here.
class SkillsViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class SubSkillsViewSet(viewsets.ModelViewSet):
    queryset = SubSkill.objects.all()
    serializer_class = SubSkillSerializer