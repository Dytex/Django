from rest_framework import serializers
from . models import tanks

class tanksSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = tanks
        fields = ('id', 'nom', 'pays', 'cat', 'desc', 'url')