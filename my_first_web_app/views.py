from django.http import HttpResponse, HttpResponseRedirect
from django.urls import path
from django.shortcuts import render
from random import randint

def root(request):
    return HttpResponseRedirect('/home')

def gallery(request):
    return HttpResponseRedirect('/portfolio')

def home_page(request):
    context = {'name': 'Adam Cote'}
    response = render(request, 'index.html', context)
    return HttpResponse(response)

def portfolio(request):
    image_urls = []
    for i in range(5):
        random_number = randint(0,100)
        image_urls.append("https://picsum.photos/400/600/?image={}".format(random_number))

    context = {'gallery_images': image_urls}
    response = render (request, 'gallery.html',context)
    return HttpResponse(response)
def about(request):
    context = {
        'skills': ['programming', 'hockey', 'video games'],
        'interests': ['hockey', 'coding', 'the internet']
    }
    response = render(request, 'about.html', context)
    return HttpResponse(response)


def favourites(request):
    context = { 'favelink': ['http://www.reddit.com',"http://www.twitter.com"]}
    response = render(request, 'favourites.html', context)
    return HttpResponse(response)
