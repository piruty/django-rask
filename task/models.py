from django.db import models

class List(models.Model):
    '''タスクのリスト'''
    title = models.CharField(u'リスト名', max_length=255)

    def __str__(self):
        return self.title

class Task(models.Model):
    '''タスク'''
    title = models.CharField(u'タスクタイトル', max_length=255)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title
