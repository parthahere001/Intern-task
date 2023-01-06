from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from .forms import CreateUserForm
from django.shortcuts import redirect
from dash.forms import CreateUserForm
from .models import Products





def home(request):
  if request.user.is_authenticated:
   allproducts = Products.objects.all()
   context = {
    'allproducts': allproducts,
   }
   return render(request, 'dashboard.html', context)
  else:
    return render(request, 'login.html')

def register(request):
  form = CreateUserForm()
  if request.method == 'POST':
    form = CreateUserForm(request.POST)
    if form.is_valid():
      new_user = form.save()
      messages.info(request, "Thanks for registering. You are now logged in.")
      new_user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],)
      login(request, new_user)
      return redirect('home')
  context = {'form':form}
  return render(request, 'register.html',context)


def filterpage(request):
  return render(request, 'filter.html')

def filterdata(request):
  pricefilter = request.POST['textdata']
  allproducts = Products.objects.filter(price__lt=pricefilter)
  context = {
    'allproducts': allproducts,
   }
  return render(request, 'dashboard.html', context)

def filterdataq(request):
  quantityfilter = request.POST['textdata']
  allproducts = Products.objects.filter(quantity__gt=quantityfilter)
  context = {
    'allproducts': allproducts,
   }
  return render(request, 'dashboard.html', context)


def filteroptions(request):
  categoryfilter = request.POST['textdata']
  allproducts = Products.objects.filter(productcategory=categoryfilter)
  context = {
    'allproducts': allproducts,
   }
  return render(request, 'dashboard.html', context)

def userlogin(request):
  if request.method=="POST":
        # Get the post parameters
      loginusername=request.POST['loginusername']
      loginpassword=request.POST['loginpassword']

      user=authenticate(username= loginusername, password= loginpassword)
      if user is not None:
          login(request, user)
          messages.success(request, "Successfully Logged In")
          return redirect("home")
      else:
          messages.error(request, "Invalid credentials! Please try again")
          return redirect("userlogin")
  return render (request,'login.html')
	
	
def userlogout(request):
    logout(request)
    return redirect('home')
