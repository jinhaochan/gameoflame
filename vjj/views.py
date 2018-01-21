from django.shortcuts import render
from django.http import HttpResponse
from .dec import checkLogin

@checkLogin
def index(request, *args, **kwargs):
    return render(request, 'index.html', kwargs['data'])

def about(request):
    return render(request, 'about.html')

@checkLogin
def c1(request, *args, **kwargs):
    return render(request, 'contestant1.html', kwargs['data'])

@checkLogin
def c2(request, *args, **kwargs):
    return render(request, 'contestant2.html', kwargs['data'])

@checkLogin
def s1(request, *args, **kwargs):
    return render(request, 'season1.html', kwargs['data'])

@checkLogin
def s2(request, *args, **kwargs):
    return render(request, 'season2.html', kwargs['data'])

@checkLogin
def s3(request, *args, **kwargs):
    return render(request, 'season3.html', kwargs['data'])

@checkLogin
def alls(request, *args, **kwargs):
    return render(request, 'allseasons.html', kwargs['data'])

@checkLogin
def login(request, *args, **kwargs):
    return render(request, 'login.html', kwargs['data'])

@checkLogin
def suggest(request, *args, **kwargs):
    return render(request, 'suggest.html', kwargs['data'])

def updateSession(request):
    if request.method == 'POST':
        if 'stat' in request.POST:
            if request.POST['stat'] == 'login':
                request.session['name'] = request.POST['name']
                request.session['logged_in'] = True
            elif request.POST['stat'] == 'logout':
                request.session['logged_in'] = False
    return render(request, 'index.html')
