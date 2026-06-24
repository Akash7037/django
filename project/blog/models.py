from django.db import models
class data (models.Model):
    title = models.CharField(100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
# Create your models here.
