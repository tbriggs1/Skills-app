# Generated by Django 3.1.7 on 2021-04-01 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skillsapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Skills',
            new_name='Skill',
        ),
        migrations.RenameModel(
            old_name='SubSkills',
            new_name='SubSkill',
        ),
    ]
