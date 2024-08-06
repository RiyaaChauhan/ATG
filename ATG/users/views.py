from django.shortcuts import render,redirect
from mainapp.models import Doctor
from django.views.decorators.cache import cache_control
from . models import Blog
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def doctorhome(request):
    try:
        if request.session["username"]!=None:
            username=request.session["username"]
            doctorreg=Doctor.objects.get(emailaddress=username)
            return render(request,"doctorhome.html",locals())
    except KeyError:
        return redirect("mainapp:login")
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def dviewprofile(request):
    try:
        if request.session["username"]!=None:
            username=request.session["username"]
            doctorreg=Doctor.objects.get(emailaddress=username)
            if request.method=="POST":
                firstname=request.POST["firstname"]
                lastname=request.POST["lastname"]
                emailaddress=request.POST["emailaddress"]
                password=request.POST["password"]
                city=request.POST["city"]
                state=request.POST["state"]
                pincode=request.POST["pincode"]
                Doctor.objects.all()
                return redirect("doctorapp:doctorhome")
            return render(request,"dviewprofile.html",locals())
    except KeyError:
        return redirect("mainapp:login") 
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def myblog(request):
    try:
        if request.session["username"]!=None:
            username=request.session["username"]
            if request.method=="POST":
                title=request.POST["title"]
                image=request.FILES["image"]
                category=request.POST["category"]
                summary=request.POST["summary"]
                content=request.POST["content"]
                blog=Blog(title=title,image=image,category=category,summary=summary,content=content)
                blog.save()
                msg="Blog Posted Successfully"
                return render(request,"myblog.html",locals())
            return render(request,"myblog.html",locals())
    except KeyError:
        return redirect("mainapp:login")
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def viewblog(request):
    try:
        if request.session["username"]!=None:
            username=request.session["username"]
            blog=Blog.objects.all()
            return render(request,"viewblog.html",locals())
    except KeyError:
        return redirect("mainapp:login")