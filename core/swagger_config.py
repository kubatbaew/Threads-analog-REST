from drf_yasg import openapi, views
from rest_framework import permissions


schema_view = views.get_schema_view(
   openapi.Info(
        title="Threads API",
        default_version='v1',
        description="This API provides endpoints for managing and interacting with threads. Threads are a way to organize and group related messages or conversations in an application. With this API, you can create new threads, add messages to threads, retrieve thread details, and more.",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@threads.local"),
        license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
