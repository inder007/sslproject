from django.http import HttpResponse
from django.template import loader

def homepage(request):
    template = loader.get_template('fpagecse/page22.html')
    return HttpResponse(template.render())


