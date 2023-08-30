from django.contrib.auth import get_user_model
from rest_framework import decorators, permissions, response, viewsets

from apps.users.serializers import *
from utils.permissions import IsOwner

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """ Набор видов для пользователей
    """
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    
    
    @decorators.action(methods=['PUT', 'PATCH'], detail=True)
    def change_password(self, request, pk=None):
        """Изменение пароля пользователя.

        Args:
            request (Request): Запрос, содержащий новый пароль.
            pk (int): Идентификатор пользователя (из параметра URL).

        Returns:
            Response: Ответ с сообщением об успешном обновлении пароля.
        """
        
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data)
        
        serializer.is_valid(raise_exception=True)
        new_password = serializer.validated_data['new_password']
        
        user.set_password(new_password)
        serializer.save()
        
        return response.Response({'message': 'Password updated successfully.'})
    
    
    def get_serializer_class(self):
        """ Получение класса сериализатора
        """
        
        if self.action in ('create', ):
            return UserCreateSerializer
        if self.action == 'change_password':
            return UserChangePasswordSerializer
        return UserSerializer
        

    def get_permissions(self):
        """ Получение классов разрешений
        """
        
        if self.action in ('list', 'update', 'destroy', 'partial_update', 'change_password'):
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
