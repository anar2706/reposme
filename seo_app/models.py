from django.db import models

class SEO(models.Model):
    path = models.CharField(max_length=255, unique=True, default='', blank=True, null=True)
    title = models.CharField(max_length=255, default='', blank=True, null=True)
    description = models.CharField(max_length=255, default='', blank=True, null=True)

    def __str__(self):
        return f"{self.path} | {self.title}"