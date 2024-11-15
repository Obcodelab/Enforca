from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .serializers import UserProfileSerializer, PaymentInfoSerializer
from .models import Profile, PaymentInfo


class SettingsViewSet(viewsets.GenericViewSet):

    @action(
        detail=False,
        methods=["GET"],
        permission_classes=[IsAuthenticated],
        serializer_class=UserProfileSerializer,
    )
    def get_profile(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        serializer = self.get_serializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(
        detail=False,
        methods=["PUT"],
        permission_classes=[IsAuthenticated],
        serializer_class=UserProfileSerializer,
    )
    def update_profile(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        serializer = self.get_serializer(
            instance=profile, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(
        detail=False,
        methods=["DELETE"],
        permission_classes=[IsAuthenticated],
    )
    def delete_account(self, request):
        user = request.user
        user.delete()
        return Response(
            {"message": "Your account has been deleted."},
            status=status.HTTP_204_NO_CONTENT,
        )

    @action(
        detail=False,
        methods=["post"],
        permission_classes=[IsAuthenticated],
        serializer_class=PaymentInfoSerializer,
    )
    def update_payment_info(self, request):
        user = request.user
        payment_info, created = PaymentInfo.objects.get_or_create(user=user)
        serializer = PaymentInfoSerializer(instance=payment_info, data=request.data)

        if serializer.is_valid():
            serializer.save()
            if created:
                message = "Payment information created successfully."
            else:
                message = "Payment information updated successfully."
            return Response(
                {"message": message, "data": serializer.data}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
