from rest_framework import serializers

from .models import Mentor
from school.serializers import HighSchoolSerializer, UniSerializer

class SimpleMentorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mentor
        fields = ('id','first_name', 'last_name', 'major','grad_year','email', 'linkedin','intro', 'essay_editing')

class MentorSerializer(serializers.HyperlinkedModelSerializer):
    uni = UniSerializer(required = False, read_only = False)
    class Meta:
        model = Mentor
        fields = ('id','first_name', 'last_name', 'major','grad_year','email', 'linkedin', 'uni', 'intro','preferred_mentee_grade','other_preferences',"essay_editing")

class TableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Mentor
        fields = ('first_name', 'last_name', 'major','uni','grad_year','email', 'linkedin',"essay_editing")
