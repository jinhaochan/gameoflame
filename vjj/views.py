from django.shortcuts import render
from django.http import HttpResponse
from .dec import checkLogin

@checkLogin
def index(request):
    if 'name' in request.session:
        name = request.session['name']
    else:
        name = "user"    
    return render(request, 'index.html', { "name" : name })

@checkLogin
def about(request):
    return render(request, 'about.html')

@checkLogin
def c1(request):
    return render(request, 'contestant1.html')

@checkLogin
def c2(request):
    return render(request, 'contestant2.html')

@checkLogin
def s1(request):
    return render(request, 'season1.html')

@checkLogin
def s2(request):
    return render(request, 'season2.html')

@checkLogin
def s3(request):
    return render(request, 'season3.html')

@checkLogin
def alls(request):
    return render(request, 'allseasons.html')

@checkLogin
def login(request):
    return render(request, 'login.html')

def updateSession(request):
    if request.method == 'POST':
        if 'stat' in request.POST:
            if request.POST['stat'] == 'login':
                request.session['name'] = request.POST['name']
                request.session['logged_in'] = True
            else:
                request.session['logged_in'] = False
    return HttpResponse(status=200)

@checkLogin
def suggest(request):
    return render(request, 'suggest.html')
