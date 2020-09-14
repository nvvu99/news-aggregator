from django.db import models
from news.models import Article, Category
from django.contrib.auth.models import AbstractUser
from .validators import UsernameValidator
from django.utils.translation import gettext, gettext_lazy as _


# Create your models here.
class User(AbstractUser):
    username_validator = UsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Bắt buộc. Không quá 150 ký tự. '
                    'Chỉ bao gồm chữ cái, số và dấu chấm(.).'),
        validators=[username_validator],
        error_messages={
            'unique': _("Username đã tồn tại."),
        },
    )
    email = models.EmailField(
        _('email'),
        max_length = 254,
        unique = True,
        error_messages = {
            'unique': _('Email đã tồn tại.')
        },
    )
    avatar = models.ImageField(
        upload_to = 'user-avatar/',
        blank = True,
    )
    viewed_articles = models.ManyToManyField(
        Article,
        through = 'History',
        through_fields = ('user', 'article'),
        related_name = 'viewed_articles',
        blank = True,
    )
    saved_articles = models.ManyToManyField(
        Article,
        through = 'SavedArticle',
        through_fields = ('user', 'article'),
        related_name = 'saved_articles',
        blank = True,
    )
    following_categories = models.ManyToManyField(
        Category,
        through = 'FollowingCategory',
        through_fields = ('user', 'category'),
        blank = True,
    )

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'


class History(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete = models.CASCADE, 
    )
    article = models.ForeignKey(
        Article, 
        on_delete = models.CASCADE, 
    )
    last_view = models.DateField(
        auto_now=True, 
    )

    def __str__(self):
        return str(self.user) + ' - ' + str(self.article)

    class Meta:
        unique_together = (('user', 'article'),)


class SavedArticle(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete = models.CASCADE, 
    )
    article = models.ForeignKey(
        Article, 
        on_delete = models.CASCADE, 
    )

    def __str__(self):
        return str(self.user) + ' - ' + str(self.article)

    class Meta:
        unique_together = (('user', 'article'),)


class FollowingCategory(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete = models.CASCADE, 
    )
    category = models.ForeignKey(
        Category, 
        on_delete = models.CASCADE, 
    )

    def __str__(self):
        return str(self.user) + ' - ' + str(self.category)

    class Meta:
        unique_together = (('user', 'category'),)
