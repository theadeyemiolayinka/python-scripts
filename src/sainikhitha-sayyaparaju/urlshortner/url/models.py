from django.db import models

# Create your models here.
class UrlMap(models.Model):
    url = models.CharField(max_length=100000000)
    urlShorten = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.title
