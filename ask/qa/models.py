from django.db import models
from django.contrib.auth.models import User
# Create your models here.

"""
Question - вопрос
title - заголовок вопроса
text - полный текст вопроса
added_at - дата добавления вопроса
rating - рейтинг вопроса (число)
author - автор вопроса
likes - список пользователей, поставивших "лайк"

Answer - ответ
text - текст ответа
added_at - дата добавления ответа
question - вопрос, к которому относится ответ
author - автор ответа
"""
class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    rating = models.IntegerField(4)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User)

    def __unicode__(self):
        return self.title

    #def get_absolute_url(self):
        #return '/post/%d/' % self.pk
    
    class Meta:
        #db_table = 'questions'
        ordering = ['-added_at']

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)

    #def get_absolute_url(self):
        #return '/post/%d/' % self.pk
    
    class Meta:
        #db_table = 'answers'
        ordering = ['-added_at']
