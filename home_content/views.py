from django.shortcuts import render
from home_content.models import AboutSection, Portfolio, Team

def home(request):
    about_section = AboutSection.objects.first()
    # return render(request, 'home.html', {'about_section': about_section})

    portfolios = Portfolio.objects.all()  # Fetch all portfolio items
    team_members = Team.objects.all()  # Fetch all team_members items
    return render(request, 'home.html', {
        'about_section': about_section,
        'portfolios': portfolios,  # Add portfolio items to context
        'team_members' : team_members,
    })


