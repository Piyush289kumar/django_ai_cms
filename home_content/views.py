from django.shortcuts import render
from home_content.models import AboutSection

def home(request):
    about_section = AboutSection.objects.first()
    return render(request, 'home.html', {'about_section': about_section})
