from django.shortcuts import render
from django.utils import encoding #smart_unicode
from urllib.parse import parse_qsl


from .models import Service
# Create your views here.


def about(req):
    return render(req, 'blog/about.html')

def addnoval(req):
    if req.method == 'POST':
        post = req.POST
        files = req.FILES
        s = Service()
        s.image = post['image']
        s.title = post['title']
        s.detail = post['detail']
        link = post['link']
        s.save()
        services = Service.objects.all()
        print(services)
        return render(req, 'blog/addnoval.html', { 'services': services })
    else:
        print('aaaaa')
        services = Service.objects.all()
        print(services)
        return render(req, 'blog/addnoval.html', { 'services': services })

def index(req):
    services = Service.objects.all()
    print(services)
    return render(req, 'blog/index.html', { 'services': services })


