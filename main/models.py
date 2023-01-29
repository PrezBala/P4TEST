from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django_resized import ResizedImageField

User = get_user_model()


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=40, blank=True)
    slug = slug = models.SlugField(max_length=400, unique=True, blank=True)
    bio = models.TextField()
    points = models.IntegerField(default=0)
    profile_pic = ResizedImageField(
        size=[50, 80],
        quality=100,
        upload_to="authors",
        default=None,
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.fullname)
        super(Post, self).save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=400)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    user = models.ForeignKey(Author, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
