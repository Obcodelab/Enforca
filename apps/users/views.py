from rest_framework import generics, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import (
    AllowAny,
    # IsAdminUser,
    IsAuthenticated,
    # IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import (
    CustomTokenObtainPairSerializer,
    LogoutSerializer,
    PasswordResetRequestSerializer,
    PasswordResetConfirmSerializer,
)


# Create your views here.


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserViewSet(viewsets.GenericViewSet):
    @action(
        detail=False,
        methods=["POST"],
        serializer_class=LogoutSerializer,
        permission_classes=[IsAuthenticated],
    )
    def logout(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            refresh_token = serializer.validated_data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {"message": "Logout successful."}, status=status.HTTP_205_RESET_CONTENT
            )
        except Exception as e:
            return Response(
                {"message": "Invalid token or logout failed."},
                status=status.HTTP_400_BAD_REQUEST,
            )

    @action(
        detail=False,
        methods=["POST"],
        serializer_class=PasswordResetRequestSerializer,
        permission_classes=[AllowAny],
    )
    def password_reset_request(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.send_otp()
        return Response(
            {"message": "An OTP has been sent to your email."},
            status=status.HTTP_200_OK,
        )

    @action(
        detail=False,
        methods=["POST"],
        serializer_class=PasswordResetConfirmSerializer,
        permission_classes=[AllowAny],
    )
    def password_reset_confirm(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            {"message": "Password reset successful."},
            status=status.HTTP_200_OK,
        )
