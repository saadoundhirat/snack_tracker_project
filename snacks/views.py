from django.shortcuts import render 
from django.views.generic import TemplateView , ListView
# import models
# from .models import Snack

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'
    # models = 'Snacks' # class model 

class AboutPageView(TemplateView):
    template_name = 'about.html'
    # models = 'Snacks'


# creating views using functions
# def about(request):
#     return render('', 'snacks/about.html')