from django.http import HttpResponse
from django.template import loader

def homepage(request):
    template = loader.get_template('home/homepage.html')
    return HttpResponse(template.render())


def login(request):
    template = loader.get_template('home/login.html')
    return HttpResponse(template.render())
