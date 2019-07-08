from rest_framework import serializers, status
from rest_framework.response import Response

from .models import Movie, Rating, Comments

IMDB_API_URL = 'https://www.omdbapi.com/'
API_KEY = '65825581'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('Source', 'Value')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('movie', 'comment')


class MovieSerializer(serializers.ModelSerializer):
    ratings = RatingSerializer(many=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('ratings', 'comments')


class TopSerializer(serializers.ModelSerializer):
    total_comments = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ('id', 'total_comments')

    def get_total_comments(self, obj):
        return obj.comments.count()