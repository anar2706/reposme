from django.db import models

# Create your models here.

# Create your models here.


class Question(models.Model):
    question = models.CharField(max_length = 250)
    answer = models.CharField(max_length = 250)
    weight = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")

    def __str__(self):
        return self.question
    
    class Meta:
        ordering = ['weight', '-created_date']