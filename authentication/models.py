# from django.db import models
# from .manager import UserManager
# from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     email_token = models.CharField(max_length=100, null=True, blank=True, verbose_name='Email Token')
#     last_logout_time = models.CharField(max_length=100, null=True, blank=True, verbose_name='Last Logout Time')
#     is_online = models.BooleanField(default=False, verbose_name='Is Online')
    
#     ACCOUNT_CHOICES = [
#         ('freemium', 'Freemium'),
#         ('premium', 'Premium'),
#         ('premium_plus', 'Premium Plus'),
#     ]
    
#     account_type = models.CharField(
#         max_length=20,
#         choices=ACCOUNT_CHOICES,
#         default='freemium',
#         verbose_name='Account Type'
#     )
    
#     avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name='Avatar')
#     bio = models.CharField(max_length=100, null=True, blank=True, verbose_name='Bio')
    
#     blocklist = models.ManyToManyField(
#         'self',
#         symmetrical=False,
#         related_name='blocked',
#         verbose_name='Blocked List'
#     )
#     # groups = models.ManyToManyField(Group, blank=True, related_name='user_groups')
#     # user_permissions = models.ManyToManyField(Permission, blank=True, related_name='user_permissions')
    
#     objects = UserManager()
    
#     def __str__(self):
#         return self.username


# from django.contrib.auth.models import AbstractUser,AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
# from django.db import models
# from django.contrib.auth.base_user import BaseUserManager
# class UserManager(BaseUserManager,AbstractBaseUser, PermissionsMixin):
#     use_in_migrations = True

#     def create_user(self, username, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('Email is required')
#         if not username:
#             raise ValueError('Username is required')

#         email = self.normalize_email(email)
#         username = self.normalize_username(username)
#         user = self.model(email=email, username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         return self.create_user(username, email, password, **extra_fields)



# class User(AbstractUser):
#     email_token = models.CharField(max_length=100, null=True, blank=True, verbose_name='Email Token')
#     last_logout_time = models.CharField(max_length=100, null=True, blank=True, verbose_name='Last logout Time')
#     is_online = models.BooleanField(default=False, verbose_name='Is Online')
    
#     ACCOUNT_CHOICES = [
#         ('freemium', 'Freemium'),
#         ('premium', 'Premium'),
#         ('premium_plus', 'Premium Plus'),
#     ]
    
#     account_type = models.CharField(
#         max_length=20,
#         choices=ACCOUNT_CHOICES,
#         default='freemium',
#         verbose_name='Account Type'
#     )
    
#     avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name='Avatar')
#     bio = models.CharField(max_length=100, null=True, blank=True, verbose_name='Bio')
    
#     blocklist = models.ManyToManyField(
#         'self',
#         symmetrical=False,
#         # related_name='blocked',
#         verbose_name='Blocked List'
#     )
#     groups = models.ManyToManyField(Group, blank=True, related_name='user_groups')

#     user_permissions = models.ManyToManyField(Permission, blank=True, related_name='user_permissions')

    
#     objects = UserManager()
    
#     def __str__(self):
#         return self.username
#     REQUIRED_FIELDS=[]

#user_token  logout_time is_online account_type avatar bio blocklist





# """ 
# import uuid

# def generate_unique_token():
#     return str(uuid.uuid4())

# # Example usage
# unique_token = generate_unique_token()
# print(unique_token)
# """