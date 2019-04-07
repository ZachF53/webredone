from django.db import models
from PIL import Image

#class Contact(models.Model):
#    name = models.CharField(max_length=120)
#    email = models.EmailField()
#    service = models.CharField(max_length=120)
#    message = models.TextField()

class Portfolio(models.Model):
    name = models.CharField(default="", max_length=120)
    site = models.CharField(default="", max_length=250)
    url = models.URLField()
    rate = models.FloatField()
    image = models.ImageField(
        upload_to='static/img', 
        null=True, 
        blank=True, 
        width_field="width_field", 
        height_field="height_field"
    )
    width_field = models.IntegerField(default=200)
    height_field = models.IntegerField(default=200)

    def save(self):
            super().save()  # saving image first

            img = Image.open(self.image.path) # Open image using self

            if img.height > 100 or img.width > 100:
                img = img.resize((100,100), Image.ANTIALIAS)
                img.save(self.image.path)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Portfolios"

class Services(models.Model):
    name = models.CharField(max_length=120)
    message = models.TextField(default="")
    text = models.CharField(default="", max_length=120)
    background = models.CharField(default="", max_length=120)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Services"

class Additional(models.Model):
    name = models.CharField(max_length=120)
    message = models.TextField(default="")
    text = models.CharField(default="", max_length=120)
    background = models.CharField(default="", max_length=120)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Additional Services"
