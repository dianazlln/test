from django.db import models

# Create your models here.


class art(models.Model):
    title = models.CharField('Название', max_length=50)
    full_text = models.TextField('Заявка')
    date = models.DateTimeField('Дата отправления')

    def __str__(self):
        return f'Заявка: {self.title}'


    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
