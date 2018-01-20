from django.shortcuts import render

def index(request):
    if 'user' in request.session:
        name = request.session['user']
    else:
        name = "user"    
    return render(request, 'index.html', { "name" : name })

def about(request):
    return render(request, 'about.html')

def c1(request):
    return render(request, 'contestant1.html')

def c2(request):
    return render(request, 'contestant2.html')

def s1(request):
    return render(request, 'season1.html')

def s2(request):
    return render(request, 'season2.html')

def s3(request):
    return render(request, 'season3.html')

def alls(request):
    return render(request, 'allseasons.html')

def login(request):
    return render(request, 'login.html')

def updateSession(request):
    if request.method == 'POST':
        if 'user' in request.POST:
            request.session['user'] = request.POST['user']
            request.session['logged_in'] = True
    return HttpResponseRedirect('.')

def suggest(request):
    return render(request, 'suggest.html')

def checkLogin(request):
    if 'logged_in' not in request.session or not request.session['logged_in']:
        request.session['logged_in'] = False
        page = 'login.html'
    else:
        page = 'index.html'
    return render(request, page)

