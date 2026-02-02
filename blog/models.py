from django.db import models
from ckeditor.fields import RichTextField

languages = [
    ("ES", "Español"),
    ("EN", "English"),
]


class Author(models.Model):
    first_name = models.CharField(max_length=36)
    last_name = models.CharField(max_length=36)
    email = models.CharField(max_length=150)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Tag(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    body = RichTextField(blank=True)
    date_published = models.DateField()
    repo_link = models.CharField(max_length=255, blank=True, null=True)
    banner_img = models.ImageField(upload_to="blog/banner_img", blank=True, null=True)
    card_img = models.ImageField(upload_to="blog/card_img", blank=True, null=True)
    lang = models.CharField(max_length=2, choices=languages, default="EN")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    class Meta:
        ordering = ["-date_published"]

    def __str__(self):
        return self.title

    def get_tags(self):
        return [tag.description for tag in self.tag.all()]
