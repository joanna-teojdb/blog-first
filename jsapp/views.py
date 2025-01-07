from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post, Category
from .forms import Postform

# Create your views here.
def index(request):
  context = {"pagename": "Index"}
  return render(request, 'jsapp/index.html', context)
  # return HttpResponse("Welcome to jsapp")

def about(request):
  context = {"pagename": "About"}
  return render(request, "jsapp/about.html", context)

def gallery(request):
  context = {"pagename": "Gallery"}
  return render(request, "jsapp/gallery.html", context)

def contact(request):
  context = {"pagename": "Contact"}
  return render(request, "jsapp/contact.html", context)

# Dopytac jak to zrobic zeby pojawiala sie sent_contact.html po submit
def sent_contact(request):
  contact_name = request.GET['imie']
  contact_surname = request.GET['nazwisko']
  context = {"pagename": "Sent contact", "contact_name":contact_name, "contact_surname":contact_surname}
  return render(request, "jsapp/sent_contact.html", context)

# post views
def post_list(request):
  category_id = request.GET.get('category')
  if category_id:
    posts = Post.objects.filter(category_id=category_id)
  else:
    posts = Post.objects.all()
  categories = Category.objects.all()
  context = {"posts":posts, "categories":categories}
  return render(request, "jsapp/post_list.html", context)

def post_create(request):
  if request.method == "POST":
      form = Postform(request.POST)
      if form.is_valid():
        form.save()
        return redirect("post_list")
      else:
        form = Postform()
        return render(request, "jsapp/post_form.html", {"form": form})
  else:
      #tutaj wchodzi bo nie ma metody post
      form = Postform()
      return render(request, "jsapp/post_form.html", {"form": form})    

def post_edit(request, pk):
  post = get_object_or_404(Post, pk=pk)
  if request.method == "POST":
      form = Postform(request.POST, instance=post)
      if form.is_valid():
        form.save()
        return redirect("post_list")
      else:
        form = Postform(instance=post)
        return render(request, "jsapp/post_form.html", {"form": form})
  else:
      form = Postform()
      return render(request, "jsapp/post_list.html")    




