from django.contrib import admin
from django.urls import include, path

from core.swagger_config import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls')),
    path('auth/', include('rest_framework.urls'))
] + [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
