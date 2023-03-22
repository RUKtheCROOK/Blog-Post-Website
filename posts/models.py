from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=256)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default='Anonymous')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])