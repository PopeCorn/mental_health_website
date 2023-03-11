from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django.conf import settings

User = get_user_model()

class Journal(models.Model):
    title = models.CharField(max_length=100, default=datetime.now().strftime('%d-%m-%Y'))
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.text
