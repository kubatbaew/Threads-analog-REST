from django.contrib.auth import get_user_model
from rest_framework import permissions, response, viewsets

from apps.users.serializers import (UserCreateSerializer,
                                    UserPrivateSerializer, UserSerializer)
from utils.permissions import IsOwner

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """ Набор видов для пользователей
    """
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_serializer_class(self):
        """ Получение класса сериализатора
        """
        
        if self.action in ('create', ):
            return UserCreateSerializer
        return UserSerializer
        

    def get_permissions(self):
        """ Получение классов разрешений
        """
        
        if self.action in ('list', 'update', 'destroy', 'partial_update'):
            return [IsOwner()]
        return [permissions.AllowAny()]
    
    
    def retrieve(self, request, *args, **kwargs):
        """ Получение отдельного пользователя
        """
        
        instance = self.get_object()
        
        if instance.private_profile and instance != request.user:
            serializer = UserPrivateSerializer(instance, context={'request': request})
        else:
            serializer = self.get_serializer(instance)
            
        return response.Response(serializer.data)
    
    
    def perform_destroy(self, instance):
        """ Выполнение до удаление объекта
        """
        
        if instance.avatar:
            instance.avatar.delete()
        
        instance.delete()
