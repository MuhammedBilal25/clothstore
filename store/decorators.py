from django.shortcuts import redirect
from store.models import BasketItem
from django.contrib import messages

def signinrequired(fn):

    def wrapper(request,*args,**kwargs):

        if not request.user.is_authenticated:
            messages.error(request,"login required")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
        
    return wrapper

def owner_permission_required(fn):

    def wrapper(request,*args,**kwargs):
        
        id=kwargs.get("pk")
        basket_item_obj=BasketItem.objects.get(id=id)
        if request.user!=basket_item_obj.basket_object.owner:
            messages.error(request,"permission denied")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
        
    return wrapper


