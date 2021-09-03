from django.shortcuts import render 
from django.views.generic import ListView , DetailView
# import models
from .models import Snack

# Create your views here.
# class HomePageView(TemplateView):
#     template_name = 'home.html'
#     models = Snack # class model 

class SnackListView(ListView):
    model = Snack
    template_name = 'snack_list.html'

class DetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack
