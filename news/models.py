from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(
        max_length = 50,
        )
    slug = models.SlugField(
        max_length = 100,
        unique = True,
        blank = True,
        editable = True,
        )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'


class Publisher(models.Model):
    name = models.CharField(
        max_length = 50,
        )
    slug = models.SlugField(
        max_length = 100,
        unique = True,
        blank = True,
        editable = True,
        )
    url = models.URLField(
        max_length = 255,
        blank = True
        )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, *args, **kwargs)
        super(Publisher, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'publishers'


class Article(models.Model):
    title = models.CharField(
        max_length = 300,
        blank = True,
        )
    slug = models.SlugField(
        max_length = 255, 
        unique = True, 
        blank = True, 
        editable = True,
        )
    original_url = models.URLField(
        max_length = 300, 
        blank = True,
        )
    thumb = models.URLField(
        max_length = 300,
        blank = True,
        )
    sapo = models.TextField(
        blank = True,
        )
    category = models.ForeignKey(
        Category, 
        on_delete = models.CASCADE,
        blank = True,
        default = None,
        )
    publisher = models.ForeignKey(
        Publisher, 
        on_delete = models.CASCADE,
        blank = True,
        default = None,
        )
    body = models.TextField(
        blank = True,
        )
    published_date = models.DateTimeField(
        blank = True,
        )

    def save(self, *args, **kargs):
        self.slug = slugify(self.title)
        super(Feed, self).save(*args, **kargs)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'articles'