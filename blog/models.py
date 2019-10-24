from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=300)
    detail = models.CharField(max_length=1000)
    link = models.CharField(max_length=300)
    image = models.ImageField(null=True, blank=True, upload_to="image")
    

    def __str__(self):
        return self.title


