from django.db import models
from news.models import Article, Category
from django.contrib.auth.models import AbstractUser, User
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
    history = models.ManyToManyField(
        Article,
        related_name = 'history',
        blank = True,
    )
    saved_articles = models.ManyToManyField(
        Article,
        related_name = 'saved_articles',
        blank = True,
    )
    following = models.ManyToManyField(
        Category,
        blank = True,
    )

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'