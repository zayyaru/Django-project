from django.shortcuts import render
from .models import *

# Create your views here.

def HomePage(request):
    banner = BannerModel.objects.all()
    home_about = HomeAboutModel.objects.all()[:1]
    facts = HomeFactsModel.objects.all()[:1]
    team = HomeTeamModel.objects.all()
    testimonial = HomeTestimonial.objects.all()
    feature = Homefeature.objects.all()
    video = HomeVideo.objects.all()[:1]
    service = HomeService.objects.all()
    context = {
        'banner':banner,
        'home_about':home_about,
        'facts':facts,
        'team' : team,
        'testimonial' : testimonial,
        'feature' : feature,
        'video' : video,
        'service' : service,

    }

    return render(request, 'index.html',context)

def AboutPage(request):
    home_about = HomeAboutModel.objects.all()[:1]
    about_about = AboutAboutModel.objects.all()
    facts = HomeFactsModel.objects.all()[:1]
    team = HomeTeamModel.objects.all()
    context = {
       
        'home_about':home_about,
        'about_about':about_about,
        'facts': facts,
        'team': team, 
    }
    return render(request, 'about.html',context)


def ServicePage(request):
    home_about = HomeAboutModel.objects.all()[:1]
    service = HomeService.objects.all()
    testimonial = HomeTestimonial.objects.all()
    context = {
       
        'home_about':home_about,
        'service' : service,
         'testimonial' : testimonial,

        
        
    }
    return render(request, 'service.html',context)


def ContactPage(request):
    contact = ContactModel.objects.first()
   

    context = {
        'contact': contact,
    
    
    }

    return render(request, 'contact.html', context)





