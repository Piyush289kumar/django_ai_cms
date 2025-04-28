from django.db import models

# Create your models here.
class AboutSection(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='about/')  # Images will go to MEDIA_ROOT/about/    

    def __str__(self):
        return self.title

class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/')  # Save images under 'portfolio/' folder
    url = models.URLField(max_length=200)  # Store the URL for the project
    title = models.CharField(max_length=255, blank=True, null=True)  # Optional title for each project

    def __str__(self):
        return self.title or "No title"  # Display the title if it exists
    

class Team(models.Model):
    image = models.ImageField(upload_to='team/')  # Save images under 'team/' folder
    url = models.URLField(max_length=200)  # Store the URL for the project or team's profile
    title = models.CharField(max_length=255, blank=True, null=True)  # Optional title for each team member
    position = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  # Optional description of the team member

    def __str__(self):
        return self.title or "No title"  # Display the title if it exists
