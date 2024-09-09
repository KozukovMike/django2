from django.db import models
from ckeditor_uploader import fields


# Create your models here.
class ContentHtml(models.Model):
    content = fields.RichTextUploadingField(verbose_name='Контент')

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = 'Контент'



