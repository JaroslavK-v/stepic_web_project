from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(4, default=0)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name='likes_set')

    def __unicode__(self):
        return self.title

    #def get_absolute_url(self):
        #return '/post/%d/' % self.pk
    
    class Meta:
        #db_table = 'questions'
        ordering = ['-added_at']

    def get_url(self):
        return reverse('question', kwargs={'id': self.id})

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)

    #def get_absolute_url(self):
        #return '/post/%d/' % self.pk
    
    def __unicode__(self):
        return self.text

    class Meta:
        #db_table = 'answers'
        ordering = ['-added_at']
