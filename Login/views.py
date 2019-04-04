from django.shortcuts import redirect,render
from .models import Login
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout


import re

# Create your views here.
def register(request):
    errors = {

    }
    context = {
        'title': 'Django Login System - Register'
    }

    if request.method == "POST":
        fullname = request.POST.get("fullname", '')
        fullname_split = fullname.split(" ")
        first_name = fullname_split[0]
        if len(fullname_split) > 1:
            last_name = fullname_split[1]

        email = request.POST.get('email', '')

        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')

        if not fullname:
            errors['fullname'] = 'Please enter your fullname'


        if not validate_email(email):
            errors['password'] = 'Invalid email input'

        if not validate_password(password):
            errors['password'] = 'Invalid password input'

        if password != password2:
            errors['password2'] = 'Passwords do not match'

        
        context['errors'] = {**errors}

        if not errors:
            # User data is clean
            # check if email already exits
            try:
                user_email = Login.objects.get(email=email)

                messages.error(request, 'Email already exists')
            except Login.DoesNotExist:
                # Email is not found
                # now register new user
                login_user = Login(first_name=first_name, last_name=last_name, email=email,  is_staff=False, is_superuser=False, is_active=True)
                login_user.set_password(password)
                # activate user immediately
                login_user.save()
                
                if login_user.pk:
                    # set user session for login
                    messages.success(request, 'User successfully registered, please login here')
                    return redirect('/login')
        
    return render(request, 'login/register.html', context)


def user_login(request):
    errors = {

    }
    context = {
        'title': 'Django Login System - Login'
    }

    if request.method == "POST":
        email = request.POST.get('email', '')

        password = request.POST.get('password', '')

        if not email.strip():
            errors['email'] = 'Email is required'

        if not password:
            errors['password'] = 'Passwords is required'

        
        context['errors'] = {**errors}

        if not errors:
            # User data is clean
            # check if email already exits
            # try:
                user = authenticate(email=email, password=password)

                if not user:
                    # email and password not correct
                    messages.error(request, 'Email/Password not correct!')
                    return redirect('/login')
                else:
                    login(request, user)
                    return redirect('/')
            # except:
                # messages.error(request, 'Sorry, server error occurred')
                # return redirect('/login')

        
    return render(request, 'login/login.html', context)

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    
    return redirect('/login')


def home(request):
    Welcome_Message = 'Welcome to User Homepage!'
    return render(request, 'login/index.html', {"message": Welcome_Message})


def validate_password(pass_str):
    if len(pass_str) != 16:
        print('lenNo')
        return False
    symbols_list = ['@','#','$','%']
    numbers_len = 3
    symbols_len = 2

    if not re.match(r'^[A-Z]{2}', pass_str):
        print('no1')
        return False

    if re.match(r'[il1Lo0O\{\}\[\]\(\)\/\\\'\"\`\~\,\;\:.<>]+', pass_str):
        print('no2')
        return False

    if not re.search(r'[a-z]+', pass_str):
        print('no3')
        return False

    
    symbols_count = 0
    for _ in pass_str:
        if _ in symbols_list:
            print('no4')
            symbols_count += 1

    if symbols_count < symbols_len:
        print('no5')
        return False

    numbers_count = 0
    for _ in pass_str:
        if re.search(r'\d+', pass_str):
            print('no6')            
            numbers_count += 1

    if numbers_count < numbers_len:
        print('no7')
        return False
    
    return True

def validate_email(email_str):
    return re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email_str)


# AB$$@123ABSVasx1