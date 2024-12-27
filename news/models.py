from django.db import models

# Create your models here.
class Turlar(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
    
class Gullar(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    photo = models.ImageField('gullar/photos',blank=Turlar,null=True),
    turi = models.ForeignKey(Turlar,on_delete=models.CASCADE)   
    
    def __str__(self):
        return self.name 
