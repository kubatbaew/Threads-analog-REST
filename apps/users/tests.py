from typing import Optional

from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class UserTestCase(TestCase):
    """ Тестирование модели Пользователя
    """
    def setUp(self):
        """ Подготовка данных для тестов
        """
        self.user_data = {
            "username": "testcase",
            "display_name": "Test Case",
            "email": "test@test.com",
            "password": "testpassword",
        }
        
    def create_user(self, data: Optional[dict] = None):
        """ Создание нового пользователя
        Args:
            data (dict, optional): Дополнительные данные для пользователя.
                Если не указано, используется self.user_data. Defaults to None.
        Returns:
            User: Созданный пользователь
        """
        if not data:
            data = self.user_data
        return User.objects.create_user(**data)

    def test_user_creation(self):
        """ Проверка на создание нового пользователя
        """
        user = self.create_user()
        self.assertIsInstance(user, User)
        self.assertEqual(user.__str__(), user.username)
        self.assertEqual(user.email, "test@test.com")
