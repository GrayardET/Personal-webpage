from django.db import models


# Create your models here.
class Comments(models.Model):
    user_id = models.IntegerField()
    content = models.TextField(max_length=256)
    time = models.TimeField(auto_now_add=True)
