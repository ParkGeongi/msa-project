
from django.db import models

from blog.posts.models import Post
from security.seq_users.models import SeqUser


# Create your models here.
class View(models.Model):
    use_in_migration = True
    view_id = models.AutoField(primary_key=True)
    ip_address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(SeqUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    class Meta:
        db_table = 'blog_views'
    def __str__(self):
        return f'{self.pk} {self.ip_address} {self.created_at}'