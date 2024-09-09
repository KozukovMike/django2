from django.db import models


# Create your models here.
class Contacts(models.Model):
    contact_phone = models.CharField(max_length=20, verbose_name='Контактный телефон')
    contact_image = models.ImageField(upload_to='infoimg/', null=True)

    def __str__(self):
        return self.contact_phone

    class Meta:
        verbose_name = 'Контактный телефон'
        verbose_name_plural = 'Контактные телефоны'


class Media(models.Model):
    image = models.ImageField(upload_to='infoimg/')
    platform = models.CharField(max_length=100, verbose_name='Платформа')
    url = models.CharField(max_length=200, verbose_name='Ссылка')

    def __str__(self):
        return self.platform

    class Meta:
        verbose_name = 'Платформа'
        verbose_name_plural = 'Платформы'


class Logo(models.Model):
    image = models.ImageField(upload_to='infoimg/')
    description = models.CharField(max_length=100, verbose_name='Описание')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Логотип'
        verbose_name_plural = 'Логотипы'
