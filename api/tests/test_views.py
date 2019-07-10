import json

from django.test import TestCase
from rest_framework.test import APITestCase

from api.models import Movie, Comments, Rating

# class MoviePostTestCase(APITestCase):
#     def test_post_request(self):
#         res = self.client.post('/movies/', {'title': 'Matrix'})
#         movie = Movie.objects.get(Title='Matrix')
#         self.assertEqual(movie.Title, 'Matrix')
#         self.assertEqual(res.status_code, 201)
#         self.assertIn('Action', res.data['Genre'])

class TestFixtures(TestCase):
    def setUp(self):
        with open('api/tests/test_data.json') as f:
            movie = json.loads(f.read())
            ratings = movie.pop('Ratings')

        m = Movie.objects.create(**movie)

        for rating in ratings:
            r = Rating.objects.create(movie=m, **rating)

class MovieViewSetTestCase(TestFixtures):

    def test_movie_list(self):
        movie = Movie.objects.get(id=1)
        self.assertIsNotNone(movie)
        self.assertEqual(movie.Title, 'Matrix')

    def test_rating(self):
        ratings = Rating.objects.get(Source='Internet Movie Database')
        self.assertIsNotNone(ratings)
        self.assertEqual(ratings.Value, '8.2/10')

