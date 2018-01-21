def checkLogin(function):
    def wrap(request, *args, **kwargs):
        if 'logged_in' not in request.session or not request.session['logged_in']:
            return render(request, "login.html")
        else:
            return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
