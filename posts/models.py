from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=256)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title