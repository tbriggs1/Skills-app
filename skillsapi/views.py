from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .models import Skill, SubSkill
from .serializers import SkillSerializer, SubSkillSerializer

# Create your views here.
class SkillsViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class SubSkillsViewSet(viewsets.ModelViewSet):

    @action(detail=True, methods=['POST'])
    def rate_skill(self, request, pk=None):
        if 'stars' in request.data:

            subSkill = SubSkill.objects.get(id=pk)
            stars = request.data['stars']
            user = User.objects.get(id=1)
            print('user', user.username)



            response = {'message': 'you got the stars'}
            return Response(response, status=status.HTTP_200_OK)
        else:
            response= {'message': 'You need to add a stars'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    queryset = SubSkill.objects.all()
    serializer_class = SubSkillSerializer


