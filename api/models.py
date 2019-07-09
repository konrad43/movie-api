from django.db import models

class Movie(models.Model):
    Title = models.CharField(max_length=200)
    Year = models.CharField(max_length=50, blank=True, null=True)
    Rated = models.CharField(max_length=50, blank=True, null=True)
    Released = models.CharField(max_length=200, blank=True, null=True)
    Genre = models.CharField(max_length=200, blank=True, null=True)
    Director = models.CharField(max_length=200, blank=True, null=True)
    Writer = models.CharField(max_length=200, blank=True, null=True)
    Actors = models.CharField(max_length=200, blank=True, null=True)
    Plot = models.TextField(blank=True, null=True)
    Language = models.CharField(max_length=200, blank=True, null=True)
    Country = models.CharField(max_length=200, blank=True, null=True)
    Awards = models.CharField(max_length=200, blank=True, null=True)
    Poster = models.CharField(max_length=200, blank=True, null=True)
    Metascore = models.CharField(max_length=200, blank=True, null=True)
    imdbRating = models.CharField(max_length=200, blank=True, null=True)
    imdbVotes = models.CharField(max_length=200, blank=True, null=True)
    imdbID = models.CharField(max_length=200, blank=True, null=True)
    Type = models.CharField(max_length=200, blank=True, null=True)
    DVD = models.CharField(max_length=200, blank=True, null=True)
    BoxOffice = models.CharField(max_length=200, blank=True, null=True)
    Production = models.CharField(max_length=200, blank=True, null=True)
    Website = models.CharField(max_length=200, blank=True, null=True)
    Response = models.CharField(max_length=200, blank=True, null=True)
    Runtime = models.CharField(max_length=200, blank=True, null=True)
    totalSeasons = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.Title

    def get_test_data(self):
        return 10


class Rating(models.Model):
    Source = models.CharField(max_length=200)
    Value = models.CharField(max_length=200)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
                              related_name='ratings')


class Comments(models.Model):
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
                              related_name='comments')
