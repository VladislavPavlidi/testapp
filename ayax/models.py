from django.db import models
import uuid


class Subdivision(models.Model):
    name = models.CharField(max_length=30, verbose_name='Подразделение')
    registered = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Зарегистрировано')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Подразделения'
        verbose_name = 'Подразделение'
        ordering = ['-registered']


class Realtor(models.Model):
    id = models.AutoField(primary_key=True)
    guid = models.UUIDField(default=uuid.uuid4, editable=False)
    surname = models.CharField(max_length=30, verbose_name='Фамилия')
    name = models.CharField(max_length=30, verbose_name='Имя')
    subdivision = models.ForeignKey(Subdivision, on_delete=models.CASCADE, verbose_name='Подразделение')
    registered = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Зарегистрировано')

    class Meta:
        verbose_name_plural = 'Риэлтора'
        verbose_name = 'Риэлтор'
        ordering = ['-registered']
