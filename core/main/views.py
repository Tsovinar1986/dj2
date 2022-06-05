from asyncio.log import logger
from django.dispatch import receiver
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View, FormView, TemplateView
from .models import Category, Product, Brand, Cart
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    
    def get(self, request):
        categ = Category.objects.all()
        return render(request, self.template_name, {'categ':categ})

class CategoryView(ListView):
    template_name = 'second.html'
    
    def get(self, request, cats):
        categories = Product.objects.filter(category=cats)
        return render(request, self.template_name,  {'cats':cats, 'categoriss':categories})

class CategoryDetail(DetailView):
	template_name = 'third.html'

	def get(self, request, id):
		ca = Brand.objects.get(pk=id)
		return render(request, self.template_name, {'ca':ca})
