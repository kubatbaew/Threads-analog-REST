from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models

from apps.users.services import validate_size_image, get_path_avatar


class User(AbstractUser):
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
    )
    email = models.EmailField(
        max_length=256,
        unique=True
    )
    bio = models.TextField(
        max_length=200,
        null=True,
        blank=True,
    )
    link = models.URLField(
        max_length=256,
        null=True,
        blank=True,
    )
    private_profile = models.BooleanField(
        default=False,
    )
    
    def __str__(self):
        return f"{self.username}"    
