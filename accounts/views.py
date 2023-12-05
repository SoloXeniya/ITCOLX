from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserForm, ProfileForm, EditUserForm
from .models import Profile
from  ads.models import Ads
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def EditProfile(request, user_id):
    user = User.objects.get(id=user_id)
    profile = Profile.objects.get(user=user)
    
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Вы успешно отредактировали профиль!')
            return redirect('profile', user_id=user.id)
        else:
            messages.error(request, 'Ошибка редактирования профиля!')
            return redirect('profile', user_id=user.id)
    else:
        user_form = EditUserForm(instance=user)
        profile_form = ProfileForm(instance=profile)
    
    context = {
        "profile_form": profile_form,
        "user_form": user_form
    }
    
    return render(request, 'edit_profile.html', context)
        
        

@login_required(login_url='login')
def UserProfile(requests, user_id):
    user = User.objects.get(id=user_id)
    # profile = Profile.objects.get(user=user)
    
    context = {
        "user_context" : user,
        # "profile_context": profile,
    }
    return render(requests, 'profile.html', context)


@login_required(login_url='login')
def user_ads(request):
    #User.objects.get(id=user_id)    
    ads = Ads.objects.filter(user=request.user)
    
    context = {
        "context_ads": ads
    }
    return render(request, 'user_ads.html', context)



def SignUpUser(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        
        if user_form. is_valid():
            user = user_form.save(commit=False)
            if user.password == request.POST.get('password2'):
                user.set_password(user.password)
                user_form.save()
                
                Profile.objects.create(user=user)
                messages.success(request, 'Вы успешно зарегистрировались')
                # path("signin/", SignUpUser, name = "login")
                return redirect('login')
            else:
                messages.error(request, 'Пароли не совпадают!')
                # path("signup/", SignUpUser, name = "register")
                return redirect('register')
        else:
            messages.error(request, "Ошибка регистрации")
            return redirect("register")
    else:
        user_form = UserForm()
        
    return render(request, 'register.html', {'context_form': user_form})

        
def SignInUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Вы успешно вошли!')
                return redirect("home")
            else:
                messages.error(request, 'Неверное имя пользователя или пароль.')
        else:
            messages.warning(request, 'Пожалуйста, введите имя пользователя и пароль.')
            return redirect("login")
    return render(request, "login.html") 
        
        
def SignOutUser(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Вы успешно вышли из учетной записи!')
        return redirect("home")
    else:
        messages.error(request, 'Вы не авторизованы!')
        return redirect('home')
            

        


#     return render(request, "AuthenticateUser/singin.html")

    # else:
    #     form = UserForm()
    # return render(requests, 'registration/signup.html', {'form': form})
    




#<input name = username' type = text 
#<input name = password' type = password 
        
#select * Profile where username=username and password=password