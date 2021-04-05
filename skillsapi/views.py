from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .models import Skill, SubSkill
from .serializers import SkillSerializer, SubSkillSerializer
from rest_framework import generics
import requests

# Create your views here.
class SkillsViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    filter_fields = ('title', 'studID')


    # def get_queryset(self):
    #     """
    #     Optionally restricts the returned purchases to a given user,
    #     by filtering against a `username` query parameter in the URL.
    #     """
    #     queryset = Skill.objects.all()
    #     username = self.request.QUERY_PARAMS.get('username', None)
    #     if username is not None:
    #         queryset = queryset.filter(studID=username)
    #     return queryset

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




def pokemon(request):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/ditto/')
    pokemon = response.json()
    print(pokemon['abilities'])
    return HttpResponse(pokemon['abilities'])