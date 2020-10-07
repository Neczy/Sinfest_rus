from django.db import models

class Comix(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Комикс', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
#    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория') надо не надо

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Комикс'
        verbose_name_plural = 'Комиксы'
        ordering = ['-created_at']