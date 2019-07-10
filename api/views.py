from django.db.models import Count
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
    filterset_fields = ('movie_id',)


class TopViewSet(viewsets.ModelViewSet):
    serializer_class = TopSerializer
    queryset = Movie.objects.all()

    def list(self, request, *args, **kwargs):
        date = request.query_params['date']

        queryset = (
            Movie.objects
                .filter(comments__created__gte=date)
                .annotate(total_comments=Count('id'))
                .order_by('-total_comments')
        )
        # | (
        #     Movie.objects.annotate(total_comments=Count('comments'))
        #         .filter(total_comments=0)
        # )
        serializer = TopSerializer(queryset, many=True)
        return Response(serializer.data)