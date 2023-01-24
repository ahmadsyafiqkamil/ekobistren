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


class Indikator4View(generic.TemplateView):
    template_name = 'content/indikator_4.html'


class Indikator5View(generic.TemplateView):
    template_name = 'content/indikator_5.html'

class Indikator6View(generic.TemplateView):
    template_name = 'content/indikator_6.html'

class Indikator7View(generic.TemplateView):
    template_name = 'content/indikator_7.html'