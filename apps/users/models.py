from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models

from apps.users.services import validate_size_image, get_path_avatar


class User(AbstractUser):
    """ Модель Пользователя
    """
    
    first_name = None
    last_name = None
    
    
    avatar = models.ImageField(
        upload_to=get_path_avatar,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png']), validate_size_image],
        null=True,
        blank=True,
    )
    display_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="Отображаемое имя пользователя.",
    )
    email = models.EmailField(
        max_length=256,
        unique=True,
        help_text="Адрес электронной почты пользователя."
    )
    bio = models.TextField(
        max_length=200,
        null=True,
        blank=True,
        help_text="Краткая биография пользователя."
    )
    link = models.URLField(
        max_length=256,
        null=True,
        blank=True,
        help_text="Ссылка пользователя."
    )
    private_profile = models.BooleanField(
        default=False,
        help_text="Профиль пользователя приватный или нет."
    )
    
    def __str__(self):
        return f"{self.username}"
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
