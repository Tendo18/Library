from django.db import models

# Create your models here.
#CATEGORY OF BOOKS
class Category(models.Model):
    title = models.CharField(max_length= 150, )
    description = models.TextField()
    created = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.title

#BOOKS
class Books(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null =True )
    isbn = models.CharField(max_length=13)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



    
    
