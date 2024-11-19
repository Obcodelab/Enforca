from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.calender import views

router = DefaultRouter()
router.register(r"events", views.CalendarEventViewSet, basename="calendarevent")

urlpatterns = [
    path("", include(router.urls)),
]
