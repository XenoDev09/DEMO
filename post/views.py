from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
# Create your views here.

def index(request):
    return HttpResponse("Hello, welcome to the Post app!")

def list_view(request):
    context = {}
    context["posts"]=Post.objects.all().order_by("-id")
    return render(request,"post/list.html",context)

def create_view(request):
    context = {}
    form=PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("list")

    context['form']=form
    return render(request,"post/create.html",context)

def detail_view(request,id):
    context={}
    context["post"]=Post.objects.get(id=id)
    return render(request,"post/detail.html",context)

def update_view(request,id):
    context={}
    obj=get_object_or_404(Post,id=id)
    form=PostForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("list")
    context["form"]=form
    return render(request,"post/update.html",context)

def delete_view(request,id):
    context={}
    obj = get_object_or_404(Post,id=id)
    if request.method=="POST":
        obj.delete()
        return redirect("list")
    return render(request,"post/delete.html",context)
    