from django.test import TestCase
from rest_framework.test import APITestCase

from api.models import Movie, Comments, Rating

class TestFixtures(TestCase):
    def setUp(self):
        Movie.objects.create(Title='test_title')


class MovieTitleTestCase(TestFixtures):
    def test_movie_in_db(self):
        movie = Movie.objects.get(Title='test_title')
        self.assertEqual(movie.Title, 'test_title')


class RatingTestCase(TestFixtures):
    def test_rating_in_db(self):
        Rating.objects.create(
            Source='test source',
            Value='test value',
            movie=Movie.objects.get(Title='test_title')
        )
        rating = Rating.objects.get(Source='test source')
        self.assertEqual(rating.Source, 'test source')


class CommentTestCase(TestFixtures):
    def test_comment_in_db(self):
        Comments.objects.create(
            comment='test comment',
            movie=Movie.objects.get(Title='test_title')
        )
        comment = Comments.objects.get(comment='test comment')
        self.assertEqual(comment.comment, 'test comment')

