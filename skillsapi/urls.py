from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import SkillsViewSet,  pokemon, AdditionalSkillsViewSet

router = routers.DefaultRouter()
router.register('skills', SkillsViewSet)
# router.register('subskills', SubSkillsViewSet)
router.register('additionalskills', AdditionalSkillsViewSet)
# router.register('essentialskills', EssentialSkillsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('pokemon', pokemon, name='pokemon'),
]