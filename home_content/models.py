from django.db import models

# Create your models here.
class AboutSection(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='about/')  # Images will go to MEDIA_ROOT/about/

    def __str__(self):
        return self.title