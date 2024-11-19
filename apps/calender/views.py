from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from .models import CalendarEvent
from .serializers import CalendarEventSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
class CalendarEventViewSet(viewsets.GenericViewSet):
    queryset = CalendarEvent.objects.all()
    serializer_class = CalendarEventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    @action(detail=False, methods=["POST"])
    def create_event(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["GET"])
    def list_events(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
