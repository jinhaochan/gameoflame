from django.shortcuts import render

def index(request):    
    return render(request, 'index.html')

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

def suggest(request):
    if request.method == 'POST':
        request.session['logged_in'] = True
        request.session['name'] =  request.POST.get('name')
    elif 'logged_in' not in request.session:
        request.session['logged_in'] = False
    return render(request,'suggest.html' , {'logged_in':request.session['logged_in']})