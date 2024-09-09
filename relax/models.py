from django.db import models
from ckeditor import fields
from ckeditor_uploader import fields


# Create your models here.
class Slider(models.Model):
    cms_img = models.ImageField(upload_to='sliderimg/')
    cms_title = models.CharField(max_length=200, verbose_name='Заголовок')
    cms_text = models.CharField(max_length=500, verbose_name='Текст')
    cms_css = models.CharField(max_length=200, null=True, default='-', verbose_name='CSS класс')

    def __str__(self):
        return self.cms_title

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'


class ContentHtml(models.Model):
    content = fields.RichTextUploadingField(verbose_name='Контент')

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = 'Контент'
