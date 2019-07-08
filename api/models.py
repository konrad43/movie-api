from django.db import models

class Movie(models.Model):
    Title = models.CharField(max_length=200)
    Year = models.IntegerField()
    Rated = models.CharField(max_length=50)
    Released = models.CharField(max_length=200)
    Genre = models.CharField(max_length=200)
    Director = models.CharField(max_length=200)
    Writer = models.CharField(max_length=200)
    Actors = models.CharField(max_length=200)
    Plot = models.TextField()
    Language = models.CharField(max_length=200)
    Country = models.CharField(max_length=200)
    Ratings = models.CharField(max_length=200)
    Metascore = models.CharField(max_length=200)
    imdbRating = models.CharField(max_length=200)
    imdbVotes = models.CharField(max_length=200)
    imdbID = models.CharField(max_length=200)
    Type = models.CharField(max_length=200)
    DVD = models.CharField(max_length=200)
    BoxOffice = models.CharField(max_length=200)
    Production = models.CharField(max_length=200)
    Website = models.CharField(max_length=200)
    Response = models.CharField(max_length=200)

    def __str__(self):
        return self.Title


class Rating(models.Model):
    Source = models.CharField(max_length=200)
    Value = models.CharField(max_length=200)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
                              related_name='ratings')
