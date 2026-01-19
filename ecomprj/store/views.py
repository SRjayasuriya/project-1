from django.shortcuts import render,redirect
from . import models as m
from django.contrib.auth import authenticate, login ,logout 
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms 
from .form import SignUpForm, UpdateUserForm, ChangePasswordForm, UserInfoForm
from payment.form import ShippingForm 
from payment.models import ShippingAddress
import json

def home(request):
    products=m.Product.objects.all()
    return render(request,'home.html',{'products':products})

def about(request):
    return render(request,'about.html',{})

def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            user = m.Profile.objects.get(user=request.user)
            if user.old_cart:
                cart=json.loads(user.old_cart)
                request.session['cart']=cart
                request.session.modified = True   
            messages.success(request,('You Have Been Logged In!'))
            return redirect('home')
        else:
            messages.success(request,('Error occurred, Please Try Again!'))
            return redirect('login')
    else:
        return render(request,'login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,('You Have Logged Out!'))
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if(request.method=='POST'):
        form =SignUpForm(request.POST)
        if(form.is_valid()):
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,('Registered Successfully!'))
            return redirect('home')
        else:
            messages.success(request,('Try Again!'))
            return redirect('register')
    else:
        return render(request,'register.html',{'form':form})

def product(request,pk):
    product=m.Product.objects.get(id=pk)
    return render(request,'product.html',{'product':product})


def category(request,foo):
    foo=foo.replace('-',' ')
    try:
        category=m.Category.objects.get(name=foo)
        products=m.Product.objects.filter(category=category)
        return render(request,'category.html',{'products':products,'category':category})
    except:
        messages.success(request,('Category Not Found!'))
        return redirect('home')
    
def update_user(request):
    if request.user.is_authenticated:
        current_user=request.user
        user_form = UpdateUserForm(data = request.POST or None, instance=current_user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request,('Profile Updated Successfully!'))
            return redirect('home')
        return render(request,"update_user.html",{'user_form':user_form})
    else:
        messages.success(request,'You Must Be Logged In To View This Page!')
        return redirect('login')
    
def update_password(request):
    if request.user.is_authenticated:
        current_user=request.user
        if request.method=='POST':
            form = ChangePasswordForm(user=current_user, data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Password Updated Successfully!")
                login(request, current_user)
                return redirect('update_user')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                return redirect('update_password')
        else:
            return render(request,"update_password.html",{'Change_password_form':ChangePasswordForm(user=current_user)})
    else:
        messages.success(request,"You Must Be Logged In To View This Page!")
        return redirect('login')

def update_info(request):
    if request.user.is_authenticated:
        shipping, created = ShippingAddress.objects.get_or_create(user=request.user)
        form, created = UserInfoForm.objects.get_or_create(user=request.user)
        if request.method=='POST':
            shipping_form = ShippingForm(data=request.POST, instance=shipping)
            form_details = UserInfoForm(data=request.POST, instance=form)
            if shipping_form.is_valid() and form_details.is_valid():
                shipping_form.save()
                form_details.save()
                messages.success(request,('Information Updated Successfully!'))
                return redirect('home')
            else:
                messages.error(request,('Please Correct The Error Below.'))
                return redirect('update_info')
        else:
            return render(request,'update_info.html',{'shipping_form':ShippingForm(instance=shipping)})
    else:
        messages.success(request,'You Must Be Logged In To View This Page!')
        return redirect('login')
    

    