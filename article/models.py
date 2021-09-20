from django.db import models
from django.db.models.fields import EmailField

class Author(models.Model):
    fio=models.CharField(max_length=255)
    address=models.CharField(max_length=100)
    email=EmailField(unique=True)
    def __str__(self):
        return self.fio
    class Meta:
        verbose_name='Автор'
        verbose_name_plural='Авторы'

class Publication(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    create_date=models.DateTimeField(max_length=100)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    visit=models.PositiveBigIntegerField()
    image=models.ImageField(upload_to='imagefolder')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Публикация'
        verbose_name_plural='Публикации'

class Comment(models.Model):
    message=models.TextField()
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    publication=models.ForeignKey(Publication,on_delete=models.CASCADE) 
    date=models.DateTimeField()  

    def __str__(self):
        return self.message
    class Meta:
        verbose_name='Коммент'
        verbose_name_plural='Комменты'

class Readers(models.Model):
    fio=models.CharField(max_length=255)
    address=models.CharField(max_length=100)
    email=EmailField(unique=True)
    def __str__(self):
        return self.fio
    class Meta:
        verbose_name='Читатель'
        verbose_name_plural='Читатели' 
        print 
    
              



