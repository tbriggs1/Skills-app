from django.contrib import admin
from .models import Skill, AdditionalSkill

admin.site.register(Skill),
# admin.site.register(SubSkill),
admin.site.register(AdditionalSkill),
# admin.site.register(EssentialSkill)