from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
import requests

from .serializers import MovieSerializer
from .models import Movie, Rating

IMDB_API_URL = 'https://www.omdbapi.com/'
API_KEY = '65825581'


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def create(self, request, *args, **kwargs):
        title = request.data['title'].replace(' ', '+').lower()
        # check if imdb api works
        params = {
            'apikey': API_KEY,
            't': title
        }
        res = requests.get(IMDB_API_URL, params=params)
        ratings = res.json().pop('Ratings')
        serializer = MovieSerializer(**res.json())

        for rating in ratings:
            r = Rating.objects.create(**rating)
            serializer.movie.add()


        return Response(serializer.data, status=status.HTTP_201_CREATED)

        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)