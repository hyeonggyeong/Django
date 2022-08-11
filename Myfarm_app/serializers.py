from .models import ImageModel, Person
from rest_framework import serializers
import base64
from Myfarm_proj import settings


class PersonSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Person
        fields = ('first_name', 'last_name','image')



