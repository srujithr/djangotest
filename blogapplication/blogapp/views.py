from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login
from .models import Bloguser

from .models import Blog

def index(request):
    return render(request, 'index.html')

def userindex(request):
    return render(request, 'user/user.html')

def user_register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        password = request.POST['password']

        data = Bloguser.objects.create_user(first_name=first_name,last_name=last_name,username=username,phone=phone,email=email,address=address,password=password)
        data.save()
        return redirect(user_login)
    else:
        return render(request, 'Register.html')





def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin:index')
            else:

                return redirect(userindex)
        else:
            return render(request,'login.html', {'error_message': 'Invalid credentials'})

    return render(request, 'login.html')

def aaa(request):
    return render(request,'user/add.html')

def add_blog(request):
    user = Bloguser.objects.get(id=request.user.id)
    print("---------------------",user)
    if request.method == 'POST':
        image = request.FILES['image']
        Title = request.POST['Title']
        Description = request.POST['Description']
        blogs = Blog.objects.create(image=image,Title=Title,Description=Description,user_id=user)
        blogs.save()
        print(blogs)
        # Redirect to the index page after adding a blog post
        return redirect(Bloglist)
    else:
        return render(request, 'user/add.html',{'user':user})


def edit_Blog(request,id):
    user = Bloguser.objects.get(id=request.user.id)
    print(user)
    datas = Blog.objects.get(id=id)
    print(datas)
    if request.method == 'POST':
        image = request.POST['image']
        Title = request.POST['Title']
        Description = request.POST['Description']
        datas = Blog.objects.update(image=image,Title=Title,Description=Description)
        return redirect(view_blog)
    else:
        return render(request, 'user/edit.html',{'datas':datas})
       

def view_blog(request):
    users = Bloguser.objects.get(id=request.user.id)
    print(users)
    data = Blog.objects.filter(user_id=users.id)
    print(data)
    return render(request, 'user/viewblog.html',{'data': data})

def delete(request,id):
    datas = Bloguser.objects.get(id=request.user.id)
    user = Blog.objects.filter(id=id)
    user.delete()
    return redirect(view_blog)

def Bloglist(request):
    user = Bloguser.objects.get(id=request.user.id)
    data = Blog.objects.all()
    return render(request, 'user/Bloglist.html', {'data': data})