from django.shortcuts import render
from django.forms import ModelForm

from pages.models import Page

def home(request):
	return render(request, "home.html", {})

def about(request):
	return render(request, "about.html", {})

def hadis(request):
	return render(request, "hadis.html", {})	

def hasilPencarian(request):
	return render(request, "hasilPencarian.html", {'hadis':Page.objects.all()})		

