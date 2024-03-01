from django.db import models

# Create your models here.
#makemigrations - create changes and store in file
#migrate - applye the pending changes create by makemigrations
class Contact(models.Model):
    name= models.CharField(max_length=122)
    email= models.EmailField(max_length=122)
    phone= models.CharField(max_length=12)
    desc= models.TextField()
    date= models.DateTimeField()

    def __str__(self):
        return self.name
