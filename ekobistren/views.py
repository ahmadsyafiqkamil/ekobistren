from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import generic
from .forms import PondokForm
from django.urls import reverse_lazy
from .models import pondok


# Create your views here.

class DaftarPondok(generic.edit.CreateView):
    template_name = 'content/daftar_pondok.html'
    form_class = PondokForm
    success_url = reverse_lazy('ekonomi:data_pondok')


class DataPondok(generic.TemplateView):
    template_name = 'content/data_pondok.html'

    # def get_context_data(self, **kwargs):
    #     context_data = super(DataPondok, self).get_context_data(**kwargs)
    #     # print(kwargs["pk"])
    #     context_data["data"] = pondok.objects.get(pk=kwargs['pk'])
    #
    #     return context_data


class Indikator1View(generic.TemplateView):
    template_name = 'content/indikator_1.html'

    # def get_context_data(self, **kwargs):
    #     context_data = super(Indikator1View, self).get_context_data(**kwargs)
    #     # print(kwargs["pk"])
    #     context_data["data"] = pondok.objects.get(pk=kwargs['pk'])
    #
    #     return context_data


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


class EvaluasiView(generic.TemplateView):
    template_name = 'content/evaluasi.html'

    def get_context_data(self, **kwargs):
        context_data = super(EvaluasiView, self).get_context_data(**kwargs)
        context_data["data"] = pondok.objects.get(id=kwargs['pk'])
        # context_data[""]

        return context_data


def get_evaluasi(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        status = request.POST.get('status')
        data_pondok = pondok.objects.get(id=id)
        data_pondok.status = status
        data_pondok.save()
        return JsonResponse({'message': 'Data sent successfully'})


def get_indikator(request, pk):
    status = pondok.objects.get(pk=pk).status
    # print(status)
    match status:
        case 0:
            return redirect(reverse_lazy("ekonomi:indikator1"))
        case 1:
            return redirect(reverse_lazy("ekonomi:indikator1"))
        case 2:
            return redirect(reverse_lazy("ekonomi:indikator2"))
        case 3:
            return redirect(reverse_lazy("ekonomi:indikator3"))
        case 4:
            return redirect(reverse_lazy("ekonomi:indikator4"))
        case 5:
            return redirect(reverse_lazy("ekonomi:indikator5"))
        case 6:
            return redirect(reverse_lazy("ekonomi:indikator6"))
        case 7:
            return redirect(reverse_lazy("ekonomi:indikator7"))

    # return JsonResponse({'message': 'Data sent successfully'})
