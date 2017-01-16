from .models import Person, Movie, Role
from rest_framework import serializers


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Person
        fields = '__all__'
        #fields = ('name','ranking', 'birth_date')


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Movie
        #fields = '__all__'
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Role
        #fields = '__all__'
        fields = '__all__'