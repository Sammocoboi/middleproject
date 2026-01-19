from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    # кастомные модель пользователя 
    #username - уже создано в Абстрактном пользователе
    #password - уже создано в Абстрактном пользователе 
    # добавим оптициональные поля
    # спец поле для почты EmailField 
    
    email = models.EmailField(unique=True,null=False)
    # поле для большого количества текста(str)
    description = models.TextField()
    #поле для символов опр количесвта с ограничем макс 255
    phone = models.CharField(max_length=11,unique=True,blank=True,null=True)
    # 2 вида поле для картинок 
    avatar = models.ImageField(upload_to='avatar/')
    #Если не храните не у себя на сервере картинки 
    # храните их на удаленке или даете пользователю загрузить авар по ссылке
    image = models.URLField()

    # добавляем флажок аутф группы людей 
    # и также задаем related name для избежания конфликтов 
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user',
        blank=True
    )

    def __str__(self):
        return self.username
    