from django.urls import path, include
from apps.settings import views
from rest_framework.routers import DefaultRouter

APP_NAME = "apps.settings"
router = DefaultRouter()
router.register(r"settings", views.SettingsViewSet, basename="settings")

urlpatterns = [path("", include(router.urls))]
