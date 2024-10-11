from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from bot.views import LogViewSet

router = routers.DefaultRouter()
router.register(r"logs", LogViewSet, basename="logs")

schema_view = get_schema_view(
    openapi.Info(
        title="Weather Bot API",
        default_version="v1",
        description="API для просмотра истории запросов пользователей Telegram-бота погоды",
    ),
    public=True,
    permission_classes=[
        permissions.AllowAny,
    ],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
