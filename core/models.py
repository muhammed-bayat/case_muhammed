from django.db import models
 
class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.CharField(max_length=255)
    mail = models.EmailField(max_length=254)
    
    image = models.FileField(blank=True)
 
    def __str__(self):
        return self.title