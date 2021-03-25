from .models import People
from rest_framework import serializers

class PeopleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = People
        fields = ('name','age')