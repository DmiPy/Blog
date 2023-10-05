from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    images = models.ImageField(null=True, blank=True, upload_to="media/post_images")

    def __str__(self):
        return self.title







