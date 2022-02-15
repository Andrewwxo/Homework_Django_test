from django.db import models

# Create your models here.
from django.contrib.auth.models import User, AbstractUser
from django.db import models


# class ShopUserProfile(models.Model):
#     user = models.OneToOneField(User,
#                                 primary_key=True,
#                                 on_delete=models.CASCADE)
#     avatar = models.ImageField(blank=True)
#     d_birth = models.DateField(blank=True, null=True)
#     bio = models.TextField(blank=True)


class ShopUser(AbstractUser):
    email = models.EmailField('email address', unique=True)
    d_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True)
