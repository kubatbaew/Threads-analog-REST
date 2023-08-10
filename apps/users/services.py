from django.core.exceptions import ValidationError


def validate_size_image(file_obj):
    megabite_limit = 5
    if file_obj.size > megabite_limit * 1024 * 1024:
        raise ValidationError(f"Максимальный размер должен быть менее чем {megabite_limit}MB")


def get_path_avatar(instance, file):
    return f"avatar/{instance.id}/{file}"
