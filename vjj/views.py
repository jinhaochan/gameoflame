from django.shortcuts import render
from django.http import HttpResponse
from .dec import checkLogin

@checkLogin
def index(request, *args, **kwargs):
    return render(request, 'index.html', kwargs['data'])

@checkLogin
def about(request, *args, **kwargs):
    return render(request, 'about.html')

@checkLogin
def c1(request, *args, **kwargs):
    return render(request, 'contestant1.html')

@checkLogin
def c2(request, *args, **kwargs):
    return render(request, 'contestant2.html')

@checkLogin
def s1(request, *args, **kwargs):
    return render(request, 'season1.html')

@checkLogin
def s2(request, *args, **kwargs):
    return render(request, 'season2.html')

@checkLogin
def s3(request, *args, **kwargs):
    return render(request, 'season3.html')

@checkLogin
def alls(request, *args, **kwargs):
    return render(request, 'allseasons.html')

@checkLogin
def login(request, *args, **kwargs):
    return render(request, 'login.html')

@checkLogin
def suggest(request, *args, **kwargs):
    return render(request, 'suggest.html')

def updateSession(request):
    if request.method == 'POST':
        if 'stat' in request.POST:
            if request.POST['stat'] == 'login':
                request.session['name'] = request.POST['name']
                request.session['logged_in'] = True
            elif request.POST['stat'] == 'logout':
                request.session['logged_in'] = False
    return render(request, 'index.html')
