from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.forms import ValidationError

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, username):
        if not email:
            raise ValueError("Email Required!!")

        if not username:
            raise ValueError("Username is required!")

        email = self.normalize_email(email)

        # Check if the email already exists
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Email must be unique.")

        # Check if the username already exists
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError("Username must be unique.")

        # Check if the password already exists
        if CustomUser.objects.filter(password=password).exists():
            raise ValidationError("Password must be unique.")

        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, username):
        user = self.create_user(email, password, username)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    username = models.CharField(unique=True, max_length=25)
    email = models.EmailField(unique=True, max_length=255)
    password = models.CharField(unique=True, max_length=255)

    USERNAME_FIELD = "email"  # set email as username
    REQUIRED_FIELDS = ["username"]
    objects = CustomUserManager()
