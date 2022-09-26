from pyexpat.errors import messages
from django.shortcuts import render,redirect
from catalog.models import Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def signUp(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        customer = User.objects.create_user(username,email,password)
        customer.save()

        return redirect('login')

    product = Product.objects.all()
    context = {'product': product}

    return render(request, 'catalog/catalog.html', context)

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            username = user.username

            return redirect('/')
        else:
            # messages.error(request, "Bad Credentials")
            return redirect('login')

    product = Product.objects.all()
    context = {'product': product}

    return render(request, 'catalog/catalog.html', context)


def logout(request):
    auth_logout(request)
    return redirect('/')