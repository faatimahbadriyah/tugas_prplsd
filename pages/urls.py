from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),
	path('hadis/', views.hadis, name='hadis'),
	path('hasil-pencarian/', views.hasilPencarian, name='hasil'),
]
