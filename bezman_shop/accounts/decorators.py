from django.shortcuts import redirect


def admin_only(function):
    def wrap(request,*args,**kwargs):

        if request.user.is_staff:
            return function(request,*args,**kwargs)
        else:
            return redirect('products')
    return wrap
