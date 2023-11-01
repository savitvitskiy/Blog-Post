from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = RichTextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    author = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comments")
    parent = models.ForeignKey("self", null=True, blank=True, related_name="replies", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author}"
