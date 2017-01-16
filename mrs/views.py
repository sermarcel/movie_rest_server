from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from mrs.serializers import PersonSerializer, MovieSerializer, RoleSerializer
from rest_framework import status
from mrs.models import Person, Movie, Role
from django.http import Http404
from rest_framework import generics

'''
class PersonListView(APIView):

    def get(self, request, format=None):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonDetailsView(APIView):

    
    def get_object(self, pk):
        
        try:
            return Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            raise Http404
    
    def get (self, request, id, format=None):
        person = self.get_object(id)
        serializer = PersonSerializer(person, context={"request": request})
        return Response(serializer.data)


class MovieView(APIView):
        def get_object(self, pk):
            try:
                return Movie.objects.get(pk=pk)
            except Movie.DoesNotExist:
                raise Http404
        
        def get (self, request, id, format=None):
            person = self.get_object(id)
            serializer = MovieSerializer(person, context={"request": request})
            return Response(serializer.data)

'''
class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetail(generics.RetrieveDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonDetail(generics.RetrieveDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class RoleList(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class RoleDetail(generics.RetrieveDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer