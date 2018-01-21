from django.shortcuts import render

def checkLogin(function):
    def wrap(request, *args, **kwargs):
        if 'logged_in' not in request.session or not request.session['logged_in']:
            request.session['logged_in'] = False  
            return render(request, "login.html")
        else:
            name = request.session['name']
            logged_in = request.session['logged_in']

            data = { 'name' : name,
                     'logged_in': logged_in
                   }

            return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
