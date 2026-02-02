from django.contrib import admin
from blog.models import Post, Author, Tag
from projects.models import Project

# Register your models here.
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Project)