from django.db import models
from apps.users.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")
    bio = models.TextField(blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user.email} Profile"


class PaymentInfo(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="payment_info"
    )
    account_number = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=100)
    billing_period = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.email}'s Payment Information"
