from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
import requests

from .serializers import MovieSerializer, CommentSerializer, TopSerializer
from .models import Movie, Rating, Comments

IMDB_API_URL = 'https://www.omdbapi.com/'
API_KEY = '65825581'


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def create(self, request, *args, **kwargs):
        if Movie.objects.get(Title__iexact=request.data['title']):
            return Response('Movie already exists')

        title = request.data['title'].replace(' ', '+').lower()
        # check if imdb api works
        params = {
            'apikey': API_KEY,
            't': title
        }
        res = requests.get(IMDB_API_URL, params=params).json()
        ratings = res.pop('Ratings')
        movie = Movie.objects.create(**res)
        serializer = MovieSerializer(movie)

        for rating in ratings:
            r = Rating.objects.create(movie=movie, **rating)



        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer


class TopViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = TopSerializer