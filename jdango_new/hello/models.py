from django.db import models

# Create your models here.

class Hello(models.Model):
    use_in_migrations = True #db로 이주시키는것 creat 쿼리문 과 같은것
    hello = models.CharField(primary_key=True, max_length=30)
    name = models.TextField()

    class Meta:
        db_table = 'hellos'

    def str(self):
        return f'{self.pk} {self.hello}'
