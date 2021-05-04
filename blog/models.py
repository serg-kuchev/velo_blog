from django.db import models
from django.utils.text import slugify


class Post(models.Model):

    class Meta():
        db_table = 'post'
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        ordering = ['-published_at']

    id = models.IntegerField(verbose_name="ID", primary_key=True)
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    update = models.DateTimeField(auto_now_add=True, verbose_name='Обновлено')
    image = models.ImageField(upload_to='post/', blank=True, verbose_name='Изображение')
    moder = models.BooleanField(default=False, verbose_name='Модерация')


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
