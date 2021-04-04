from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import SkillsViewSet, SubSkillsViewSet, pokemon

router = routers.DefaultRouter()
router.register('skills', SkillsViewSet)
router.register('subskills', SubSkillsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('pokemon', pokemon, name='pokemon'),
]