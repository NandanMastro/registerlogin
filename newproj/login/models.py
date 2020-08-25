from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have a password')


        print('Details received by model')
        print('email = ', email)
        print('password = ', password)


        user = self.model(email=self.normalize_email(email), password=password)
        user.set_password(password)
        # print(user.password)

        user.save(using=self._db)
        return user

        # user.set_password(password)
        # user.save(using=self._db)
        # return user

    def create_superuser(self, email, password):

        user = self.create_user(email=self.normalize_email(email), password=password)
        print('superuser')
        user.is_verified = True
        user.is_active = True
        user.is_superuser = True
        user.is_admin = True

        user.save(using=self._db)
        return user


# Create your models here.
class account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    phone_no = models.CharField(verbose_name="phone_no", max_length=13)

    password = models.CharField(verbose_name="password", max_length=255)
    otp = models.CharField(verbose_name="otp", max_length=10, null=True, default="genOTP()")

    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['password']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    # For checking permissions. to keep it simple all admin have ALL permissions
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True


class User_info(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name
