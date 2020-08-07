from django.db import models
import uuid
import secrets
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.timezone import now

# Create your models here.


class CustomUserManager(UserManager):

    def generate_api_key(self, user_id):
        api_key = secrets.token_hex(32)
        user = self.filter(pk=user_id)
        if user:
            user.update(api_key=api_key)
            return api_key
        else:
            return "User Not Found"


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    api_key = models.CharField(max_length=64, null=True, blank=True, unique=True)
    objects = CustomUserManager()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        managed = True
        db_table = "users"
        app_label = "user"


class Activity(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="activity_periods")
    start_time = models.DateTimeField(null=False, blank=False, default=now)
    end_time = models.DateTimeField(null=True, blank=False)

    class Meta:
        managed = True
        app_label = "user"

