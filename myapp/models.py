from django.db import models

# Create your models here.
class BannerModel(models.Model): 
    bg = models.ImageField(upload_to='banner/')
    tag = models.CharField(max_length=200)
    des = models.TextField()
    more = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.tag
    
class HomeAboutModel(models.Model):
    title = models.CharField(max_length=200)
    dec = models.TextField()
    years = models. TextField()   
    email = models.EmailField()
    phone = models.TextField()
    tag1 = models.CharField(max_length=200 , null=True,blank=True)
    tag2 = models.CharField(max_length=200 , null=True,blank=True)
    tag3 = models.CharField(max_length=200 , null=True,blank=True)
    tag4 = models.CharField(max_length=200 , null=True,blank=True)
    tag5 = models.CharField(max_length=200 , null=True,blank=True)
    img1 = models.ImageField(upload_to='HomeAbout/')
    img2 = models.ImageField(upload_to='HomeAbout/')

    def __str__(self):
        return self.title
    
class HomeFactsModel(models.Model):
    years = models.CharField(max_length=200)
    team = models.CharField(max_length=200)
    clients = models.CharField(max_length=200)
    project = models.CharField(max_length=200)

    def __str__(self):
        return self.years

class HomeTeamModel(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    image = models.ImageField(upload_to='HomeTeam/')
    viber = models.URLField()
    whatapps = models.URLField()
    linkedin = models.URLField()

    def __str__(self):
        return self.name

class HomeTestimonial(models.Model):
    image = models.ImageField(upload_to='Hometestimonial/')
    name = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    des = models.TextField()

    def __str__(self):
        return self.name

class Homefeature(models.Model):
    title = models.CharField(max_length=200)
    des = models.TextField()

    def __str__(self):
        return self.title     

class HomeVideo(models.Model):
    title = models.CharField(max_length=200)
    des = models.TextField()
    image = models.ImageField(upload_to='Homevideo/')
    video = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title           


class HomeService(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Hometitle/')
    des = models.TextField()

    def __str__(self):
        return self.title

class AboutAboutModel(models.Model):
    
    tag = models.CharField(max_length=200 , null=True,blank=True)
    
    def __str__(self):
        return self.tag   

class ContactModel(models.Model):
    
    phone = models.TextField()
    
    
    def __str__(self):
        return self.phone 


