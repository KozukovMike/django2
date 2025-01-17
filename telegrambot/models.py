from django.db import models


# Create your models here.
class TelegramSettings(models.Model):
    tg_token = models.CharField(max_length=100, verbose_name='Телеграм токен')
    tg_chat = models.CharField(max_length=100, verbose_name='Id чата')
    tg_message = models.CharField(max_length=200, verbose_name='Сообщение')

    def __str__(self):
        return self.tg_chat

    class Meta:
        verbose_name = 'Настройку'
        verbose_name_plural = 'Настройки'

