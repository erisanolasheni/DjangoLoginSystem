from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.


class BaseModel(models.Model):
    # create the timestamp fields
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)


class Login(BaseModel, AbstractUser):

    # define whether the user should be activated or not
    is_active = models.BooleanField(default=True)
    # changes email to unique and blank to false
    email = models.EmailField(unique=True, null=True)
    username = models.CharField(null=True, max_length=100, blank=True)
    password = models.CharField(max_length=100, null=False, blank=False)

    is_staff = models.BooleanField(default=False)

    is_active=models.BooleanField(
        default=True,
    )

    USERNAME_FIELD='email'

    REQUIRED_FIELDS = []

    objects=UserManager()

    class Meta():
        ordering=["-pk"]
