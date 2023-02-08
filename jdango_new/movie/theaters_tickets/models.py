from django.db import models

# Create your models here.
from django.db import models

from security.seq_users.models import SeqUser


# Create your models here.
class Theater_ticket(models.Model):
    use_in_migration = True
    theater_ticket_id = models.AutoField(primary_key=True)#auto increment 되는 IntegerField이다
    x = models.IntegerField()
    y = models.IntegerField()
    user = models.ForeignKey(SeqUser, on_delete=models.CASCADE)
    class Meta:
        db_table = 'movie_theater_tickets'

    def __str__(self):
        return f'{self.pk} {self.x} {self.y}'

