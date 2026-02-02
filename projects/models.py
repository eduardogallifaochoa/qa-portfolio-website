from django.db import models
from blog.models import Post

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    showcase = models.BooleanField(default=False)
    live_demo = models.CharField(max_length=255, null=True, blank=True)
    post = models.OneToOneField(
        Post,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.title