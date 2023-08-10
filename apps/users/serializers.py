from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """ Сериализатор пользователей
    """
    
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'display_name',
            'avatar',
            'email',
            'bio',
            'link',
            'private_profile'
        )


class UserCreateSerializer(serializers.ModelSerializer):
    """ Сериализатор создание пользователей
    """
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = (
            'username',
            'display_name',
            'email',
            'password',
        )
        
    def create(self, validated_data):
        """ Хеширование пароля при создании пользователя
        """
        password = validated_data['password']
        if not password:
            raise serializers.ValidationError("[ERROR]!: Not Password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        
        return user
    
    def validate_username(self, value):
        """ Валидация и преобразование username в нижний регистр.
        """
        return value.lower()
    

class UserPrivateSerializer(serializers.ModelSerializer):
    """ Сериализатор для приватных пользоватлей
    """
    
    class Meta:
        model = User
        fields = (
            'username',
            'avatar',
            'bio',
        )
