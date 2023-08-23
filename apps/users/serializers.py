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
            'id',
            'username',
            'display_name',
            'email',
            'password',
        )
        read_only_fields = (
            'id',
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
    """ Сериализатор для приватных пользователей
    """
    
    class Meta:
        model = User
        fields = (
            'username',
            'avatar',
            'bio',
        )


class UserChangePasswordSerializer(serializers.ModelSerializer):
    """ Сериализатор для изменения пароля
    """
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    new_password_repeat = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = (
            'old_password',
            'new_password',
            'new_password_repeat',
        )
    
    def validate(self, attrs):
        """ Проверка паролей на сходство
        """
        user = self.context['request'].user
        old_password = attrs.get('old_password')
        new_password = attrs.get('new_password')
        new_password_repeat = attrs.get('new_password_repeat')
        
        if new_password != new_password_repeat:
            raise serializers.ValidationError("The new passwords do not match. Please try again!")
        
        if not user.check_password(old_password):
            raise serializers.ValidationError("The old password does not match the current password!")
        
        return attrs
    
    def update(self, instance, validated_data):
        """ Хеширование пароля при сохранении
        """
        new_password = validated_data['new_password']
        instance.set_password(new_password)
        instance.save()
        return instance
