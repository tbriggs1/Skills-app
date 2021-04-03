from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from .models import Skill, SubSkill
from .serializers import SkillSerializer, SubSkillSerializer

# Create your views here.
class SkillsViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    @action(detail=True, methods=['POST'])
    def rate_skill(self, request, pk=None):
        if 'title' in request.data:

            skill = Skill.objects.get(id=pk)
            print('Skill title', skill.title)
            response = {'message': 'its working'}
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'You need to provide stars'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class SubSkillsViewSet(viewsets.ModelViewSet):
    queryset = SubSkill.objects.all()
    serializer_class = SubSkillSerializer


