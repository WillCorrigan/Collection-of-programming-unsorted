from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name



class Topic(models.Model):
    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Comment(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)


    def __str__(self):
        return str(self.topic) + ' - ' + str(self.created_by) + ' - post number ('+ str(self.pk) + ') - ' + self.message[0:15] 

    def get_absolute_url(self):
        return reverse('forum-thread', kwargs={'pk2': self.topic.pk, 'pk':self.topic.board.pk}) +"?page=last"