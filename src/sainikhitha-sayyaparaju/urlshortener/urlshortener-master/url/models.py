from django.db import models

# Create your models here.


class url_db(models.Model):
    og = models.URLField()
    short = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.short
