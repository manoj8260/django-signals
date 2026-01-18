from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)
    tags = models.ManyToManyField(Tag, related_name="posts", blank=True)

    def __str__(self):
        return self.title


class DeletedPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    deleted_at = models.DateTimeField()

    def __str__(self):
        return f"Deleted: {self.title}"
