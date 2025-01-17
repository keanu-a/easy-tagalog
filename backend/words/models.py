from django.db import models

# Create your models here.
class Word(models.Model):
    tagalog = models.CharField(max_length=60)
    english = models.CharField(max_length=60)
    
    def __str__(self):
        return self.tagalog