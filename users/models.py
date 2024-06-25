from django.contrib.auth.models import AbstractUser
from django.db import models


class Permission(models.Model):
    """
    This model represents a permission within the system.
    """
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Role(models.Model):
    """
    This model represents a user role within the system.
    """
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    permissions = models.ManyToManyField(Permission, related_name='roles')

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    """
    This model represents a custom user extending
    the built-in Django User model.
    """
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    roles = models.ManyToManyField(Role, related_name='users')

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # unique related_name
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # unique related_name
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

    def __str__(self):
        return self.username
