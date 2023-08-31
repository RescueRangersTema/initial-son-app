from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

from django.conf import settings


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(
            email=self.normalize_email(email), **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    name = models.CharField(max_length=255)
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name='email address'
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email


class ExcerciseArticle(models.Model):
    title = models.TextField(max_length=1000)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='excercise_article'
    )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    tags = models.ManyToManyField('Tag')
    excercises = models.ManyToManyField('Excercise', blank=True)

    class Meta:
        db_table = 'excercise_article'
        verbose_name = 'exercise_article'
        verbose_name_plural = 'exercise_articles'

    def __str__(self) -> str:
        return f'{self.title}  {self.author.email}'


class Excercise(models.Model):

    title = models.CharField(max_length=2000, null=True)

    problem = models.TextField()

    solution = models.TextField(null=True, default=None)
    explanation_solution = models.TextField(
        null=True, default=None, blank=True, 
        help_text='Text to explain problem-solution structures'
        )

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='excercise'
    )
    is_sample = models.BooleanField(
        default=False,
        help_text='Use this excercise as sample exercise in the article. Will be shown in the text.'
        )
    class Meta:
        db_table = 'excercise'
        verbose_name = 'exercise'
        verbose_name_plural = 'exercises'

    def __str__(self) -> str:
        if self.title:
            return f'{self.title} •••••••••••••••••••• {self.author.email}'
        return f'{self.problem} •••••••••••••••••••• {self.author.email}'



class Tag(models.Model):
    title = models.TextField(max_length=200)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = 'tag'
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    def __str__(self) -> str:
        return f'-> {self.id}  {self.title}'
