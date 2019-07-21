from rest_framework import serializers
from sakila.models import Actor

class ActorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_id','first_name', 'last_name', 'last_update']