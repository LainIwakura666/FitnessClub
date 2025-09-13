from django.db import models

class Lead(models.Model):
    PURPOSE_CHOICES = [
        ('Похудение', 'Похудение'),
        ('Набор мышечной массы', 'Набор мышечной массы'),
        ('Поддержание формы', 'Поддержание формы'),
        ('Реабилитация после травм', 'Реабилитация после травм'),
        ('Подготовка к соревнованиям', 'Подготовка к соревнованиям')
    ]
    
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    phone = models.CharField(max_length=11, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Email')
    purpose = models.CharField(
        max_length=30, 
        choices=PURPOSE_CHOICES, 
        verbose_name='Цель посещения'
    )
    comment = models.TextField(blank=True, default='', verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_processed = models.BooleanField(default=False, verbose_name='Обработано')
    