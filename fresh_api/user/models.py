from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid

class TimeModel(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None, **extra_fields):
        
        if not email:
            raise ValueError('The Email field must be set')
        if not nickname:
            raise ValueError('The nickname field must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, nickname=nickname, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, nickname, password=None, **extra_fields):
        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('user_role', 2)

        
        return self.create_user(email, nickname, password, **extra_fields)

class User(AbstractBaseUser, TimeModel):
    email = models.EmailField(
        max_length=50,
        unique=True,
    )
    nickname = models.CharField(
        # 일반유저한테는 닉네임
        # 팝업담당자한테는 브랜드네임
        max_length=25,
    )
    uuid = models.UUIDField(
		default=uuid.uuid4
	)
    is_active = models.BooleanField(
        # django에서 필요한 필드
        default=True
    )
    is_staff = models.BooleanField(
        default=False
    ) 
    user_role = models.IntegerField(
        default=0,
        choices=[
            (0, '일반 유저'),
            (1, '멘토'),
            (2, '어드민')
        ]
    )
    objects = UserManager()
    USERNAME_FIELD = 'nickname'