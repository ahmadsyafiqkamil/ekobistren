from django.shortcuts import render
from django.views import generic


# Create your views here.

class HomeView(generic.TemplateView):
    template_name = 'content/home.html'


class Indikator1View(generic.TemplateView):
    template_name = 'content/indikator_1.html'


class Indikator2View(generic.TemplateView):
    template_name = 'content/indikator_2.html'

class Indikator3View(generic.TemplateView):
    template_name = 'content/indikator_3.html'