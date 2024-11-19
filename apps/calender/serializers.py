from rest_framework import serializers
from .models import CalendarEvent
from apps.users.models import User


class CalendarEventSerializer(serializers.ModelSerializer):
    user = serializers.UUIDField(source="user.id", read_only=True)
    candidate = serializers.UUIDField()

    class Meta:
        model = CalendarEvent
        fields = [
            "id",
            "title",
            "start_time",
            "end_time",
            "location",
            "video_link",
            "user",
            "candidate",
        ]

    def create(self, validated_data):
        candidate_id = validated_data.pop("candidate")
        candidate = User.objects.get(id=candidate_id)
        validated_data["candidate"] = candidate
        event = CalendarEvent.objects.create(**validated_data)
        return event
