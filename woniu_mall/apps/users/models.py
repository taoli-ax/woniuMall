from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    """ 自定义 """
    mobile = models.CharField(max_length=11, unique=True, verbose_name='phone number')

    class Meta:
        db_table = 'tb_user'
        verbose_name = 'User'

    def __str__(self):
        return self.username
