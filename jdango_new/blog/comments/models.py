from django.db import models

from blog.posts.models import Post
from security.seq_users.models import SeqUser


# Create your models here.
class Comment(models.Model):
    use_in_migration = True
    comment_id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent_id = models.TextField(null=True)

    user = models.ForeignKey(SeqUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


    class Meta:
        db_table = 'blog_comments'
    def __str__(self):
        return f'{self.pk} {self.content} {self.created_at} {self.updated_at}'