from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import LoginForm,RegistrationForm,UserProfileForm
from blog.models import BlogArticles

# Create your views here.

def user_login(requset):
    if requset.method == 'POST':
        login_form = LoginForm(requset.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])

            if user:
                login(requset,user)
                # return HttpResponse("Welcome You.You have been authenticated successfully")
                blogs = BlogArticles.objects.all()
                return render(requset,'blog/titles.html', {'blogs': blogs})
            else:
                return HttpResponse("Sorry,Your username or password is not right")

        else:
            return HttpResponse("Invalid login")

    if requset.method == 'GET':
        login_form = LoginForm()
        return render(requset,'account/login.html',{'form':login_form})

def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid()*userprofile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            return HttpResponse("Successfully")
        else:
            return HttpResponse("Sorry,you can not register.")
    else:
        user_form = RegistrationForm()
        userprofile_form = UserProfileForm()
        return render(request,'account/register.html',{'form':user_form,'profile':userprofile_form})