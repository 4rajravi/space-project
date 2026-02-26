from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("user", "User"),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="user")

    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)

    bio = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username