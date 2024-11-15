from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.users import views
from rest_framework_simplejwt.views import TokenRefreshView

APP_NAME = "apps.users"
router = DefaultRouter()
router.register(r"users", views.UserViewSet, basename="users")

urlpatterns = [
    path("", include(router.urls)),
    path("login/", views.CustomTokenObtainPairView.as_view(), name="login"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
]
