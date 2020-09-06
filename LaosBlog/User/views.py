from django.shortcuts import render, redirect
from . import models, forms


# Create your views here.
def login(request):
    if request.session.get('is_login', None):
        return redirect('')

    if request.method == "POST":
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            if username and password:
                try:
                    user = models.Users.objects.get(username=username)
                    if password == user.password:
                        request.session['is_login'] = True
                        request.session['user_id'] = user.id
                        request.session['user_name'] = user.username
                        return redirect('/')
                    else:
                        message = 'wrong password'
                except:
                    message = 'wrong username'
            return render(request, 'login.html', {'message': message})

    login_form = forms.LoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/')
    request.session.flush()
    return redirect('/')


def register(request):
    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password']
            if username and password:
                user = models.Users.objects.create()
                user.username = username
                user.password = password
                user.save()
                return redirect('/User/login/')

    register_form = forms.RegisterForm()
    return render(request, 'register.html', {'register_form': register_form})