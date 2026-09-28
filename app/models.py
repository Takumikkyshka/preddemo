from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=30, verbose_name='Номер телефона')
    third_name = models.CharField(max_length=150, verbose_name='Отчество')

name_choices = (
    ('Аудитория', 'Аудитория'),
    ('Коворкинг', 'Коворкинг'),
    ('Кинозал', 'Кинозал'),
)

payment_choices = (
    ('При посещении', 'При посещении'),
    ('СБП', 'СБП'),
)

status_choices = (
    ('Новая', 'Новая'),
    ('Мероприятие назначено', 'Мероприятие назначено'),
    ('Завершено', 'Завершено'),
)

class Zayavka(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название помещения', choices=name_choices)
    date = models.DateField(verbose_name='Дата бронирования')
    status = models.CharField(max_length=30, verbose_name='Статус заявки', choices=status_choices, default='Новая')
    payment = models.CharField(max_length=30, verbose_name='Способ оплаты', choices=payment_choices)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'Заявка пользователя {self.user.username}'

    class Meta:
        verbose_name = 'Заявка пользователя'
        verbose_name_plural = 'Заявки пользователей'

class Review(models.Model):

    text = models.TextField(verbose_name='Текст отзыва')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания отзыва')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    zayavka = models.OneToOneField(Zayavka, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return f'Отзыв пользователя {self.user.username}'

    class Meta:
        verbose_name = 'Отзыв пользователя'
        verbose_name_plural = 'Отзывы пользователей'