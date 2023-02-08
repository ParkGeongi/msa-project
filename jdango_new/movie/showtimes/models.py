from django.db import models

from movie.cinemas.models import Cinemas
from movie.movies.models import Movies
from movie.theaters.models import Theater


# Create your models here.
class Showtime(models.Model):
    use_in_migration = True
    showtime_id = models.AutoField(primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    cinema = models.ForeignKey(Cinemas, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)

    class Meta:
        db_table = 'movie_show_times'
    def __str__(self):
        return f'{self.pk} {self.start_time} {self.end_time}'
