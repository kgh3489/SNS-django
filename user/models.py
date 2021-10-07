#user/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser #Django의 기본 유저 모델
from django.conf import settings
# Create your models here.
class UserModel(AbstractUser):

    class Meta: #db 정보를 메타에 적어줌
        db_table = "my_user" #db table 이름을 지정

    # username = models.CharField(max_length=20, null=False)
    # password = models.CharField(max_length=256, null=False)
    bio = models.CharField(max_length=256, blank=True)
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followee")
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

