from django.db import models

# Create your models here.
class Movies(models.Model):
    use_in_migration = True
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    poster_url = models.CharField(max_length=255)
    running_time = models.CharField(max_length=100)
    age_rating = models.CharField(max_length=100)
    class Meta:
        db_table = 'movie_movies'
    def __str__(self):
        return f'{self.pk} {self.title} {self.director} {self.description} ' \
               f'{self.poster_url} {self.running_time} {self.age_rating}'


