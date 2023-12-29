from django.db import models
from django.contrib.auth.models import AbstractUser
from . manager import UserManager
class User(AbstractUser):
    email_token = models.CharField(max_length=255,unique=True, null=True, blank=True, verbose_name='Email Token')
    last_logout_time = models.CharField(max_length=100, null=True, blank=True, verbose_name='Last Logout Time')
    is_online = models.BooleanField(default=False, verbose_name='Is Online')
    is_updated = models.BooleanField(default=False, verbose_name='Is Updated')
    email_activated = models.BooleanField(default=False, verbose_name='Email Activated')
    ACCOUNT_CHOICES = [
        ('freemium', 'Freemium'),
        ('premium', 'Premium'),
        ('premium_plus', 'Premium Plus'),
    ]
    
    account_type = models.CharField(
        max_length=20,
        choices=ACCOUNT_CHOICES,
        default='freemium',
        verbose_name='Account Type'
    )
    
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name='Avatar')
    bio = models.CharField(max_length=100, null=True, blank=True, verbose_name='Bio')
    
    blocklist = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='blocked_by',
        verbose_name='Blocked List',
        blank=True   
    )
    
    def __str__(self):
        return self.username




""" 
import uuid

def generate_unique_token():
    return str(uuid.uuid4())

# Example usage
unique_token = generate_unique_token()
print(unique_token)
"""