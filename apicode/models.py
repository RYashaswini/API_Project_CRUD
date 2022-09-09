from django.db import models

# Create your models here.
   
    
class Article(models.Model):

    
    Shipping = (
    ('online', 'Online'),
    ('post', 'Post'),
    )

    Journal = (
    ('comic', 'Comic'),
    ('horror', 'Horror'),
    ('thriller' , 'Thriller'),
    )

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    shipping = models.CharField(max_length = 6, choices = Shipping)
    journal = models.CharField(max_length = 20, choices = Journal)
    myimage = models.ImageField(upload_to='media/', blank=True)


    def __str__(self):
        return self.title