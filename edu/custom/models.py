from django.db import models

class CustomTopic(models.Model):
    content=models.TextField()