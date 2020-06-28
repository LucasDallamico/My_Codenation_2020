from django.db import models
from django.core import validators

# Create your models here.
class User(models.Model):
    name = models.CharField('Name', max_length=50)
    last_login = models.DateTimeField('Last login',auto_now=True)
    email = models.EmailField("Email", max_length=254, validators=[validators.EmailValidator()])
    password =  models.CharField('Password', max_length=50,
                    validators=[validators.MinValueValidator(8)])


class Agent(models.Model):
    name = models.CharField('Name', max_length=50)
    status = models.BooleanField()
    env = models.CharField('Env', max_length=20)
    version = models.CharField('Version', max_length=5)
    address = models.GenericIPAddressField(protocol='IPV4')


class Event(models.Model):
    level = models.CharField(['CRITICAL', 'DEBUG', 'ERROR', 'INFO'], max_length=20)
    data = models.TextField()
    arquivado = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)
    agent = models.ForeignKey(
        Agent,
        on_delete=models.CASCADE        
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


class Group(models.Model):
    name = models.CharField('Name', max_length=50)


class GroupUser(models.Model):
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE)