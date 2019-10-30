from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50,verbose_name='ad')
    email = models.EmailField()
    content = models.TextField(verbose_name='Məzmun')

    def __str__(self):
        return self.content