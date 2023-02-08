from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Cinemas(models.Model):
    use_in_migration = True
    cinema_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    image_url = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    detail_address = models.CharField(max_length=255)

    class Meta:
        db_table = 'movie_cinemas'
    def __str__(self):
        return f'{self.pk} {self.title}  {self.image_url} {self.address} {self.detail_address}'