from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    
    
