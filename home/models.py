from django.db import models
from datetime import datetime

# Create your models here.
class Journal(models.Model):
    title = models.CharField(max_length=100, default=datetime.now().strftime('%d-%m-%Y'))
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text