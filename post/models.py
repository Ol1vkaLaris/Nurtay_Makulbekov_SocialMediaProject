from django.db import models
from django.utils import timezone
from user.models import User
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET(2), verbose_name='Автор')
    title = models.CharField(max_length=128, verbose_name='Заголовок поста')
    content = models.TextField(verbose_name='Контент поста')
    time_stamp = models.DateTimeField(default=timezone.now, verbose_name='Дата и время')
    edited = models.BooleanField(default=False, verbose_name='Изменен ли данный пост?')
    likes = models.ManyToManyField(User, blank=True, related_name='liked_post', verbose_name='Лайки поста')

    def total_likes(self):
        return self.likes.count()

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f'{self.title}: {self.time_stamp}'
    
class PostAttachments(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назание файла', blank=True)
    file = models.FileField(upload_to='images/', verbose_name='Путь к файлу')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')

    def save(self, *args, **kwargs):
        file_name = self.file.name.split('.')[0].capitalize()
        self.name = file_name
        super().save()

    class Meta:
        verbose_name = 'Файлы пост'
        verbose_name_plural = 'Файлы постов'
    

    def __str__(self):
        return f'{self.name}: {self.post}'
    
class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET(2), verbose_name='Автор')
    content = models.TextField(verbose_name='Контент комментария')
    time_stamp = models.DateTimeField(default=timezone.now, verbose_name='Дата и время')
    edited = models.BooleanField(default=False, verbose_name='Изменен ли данный пост?')
    pinned = models.BooleanField(default=False, verbose_name='Прикреплен ли данный комментарий?')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f'{self.post} : {self.content} {self.time_stamp}'
    


