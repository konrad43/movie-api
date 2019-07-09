from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
from rest_framework import viewsets, status, filters
from rest_framework.response import Response
import requests

from django.db.models.expressions import Window
from django.db.models.functions.window import RowNumber

from .serializers import MovieSerializer, CommentSerializer, TopSerializer
from .models import Movie, Rating, Comments

IMDB_API_URL = 'https://www.omdbapi.com/'
API_KEY = '65825581'


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def create(self, request, *args, **kwargs):
        if Movie.objects.all().filter(Title__iexact=request.data['title']):
            return Response('Movie already exists')

        # get data from imdb api
        title = request.data['title'].replace(' ', '+').lower()
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
    # filterset_fields = ('movie_id',)


class TopViewSet(viewsets.ModelViewSet):
    queryset = (
        Movie.objects
            .annotate(total_comments=Count('comments'))
            .order_by('-total_comments')
            # .annotate(rank=Window(expression=RowNumber()))
    )
    serializer_class = TopSerializer
