from django.db import models
from categories.models import Category
from author.models import Author

# Create your models here.
class Post(models.Model):
    tital=models.CharField(max_length=50)
    content=models.TextField()
    category=models.ManyToManyField(Category) #ekta post multiple categoryer moddhe thkte pare abar ekta categorir moddhe multiple post thkte
    author=models.ForeignKey(Author,on_delete=models.CASCADE) #jode amara akjon athor k delelt kori tahole auto post delelt hoye jai
    
    def __str__(self):
        return self.tital
