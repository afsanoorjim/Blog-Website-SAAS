from django.db import models

# Create your models here.
class Blog(models.Model):
    author = models.CharField(max_length=4000)
    title = models.CharField(max_length=4000)
    content = models.TextField()
    content_image = models.ImageField(upload_to= 'blog/media/', blank=True, null=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.title