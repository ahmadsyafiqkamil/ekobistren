from django.http import JsonResponse
from django.shortcuts import redirect
from django.views import generic
from .forms import PondokForm
from django.urls import reverse_lazy
from .models import pondok, ciri_ciri
from django.urls import reverse


# Create your views here.

class DaftarPondok(generic.edit.CreateView):
    template_name = 'content/daftar_pondok.html'
    form_class = PondokForm
    success_url = reverse_lazy('ekonomi:data_pondok')


class DataPondok(generic.TemplateView):
    template_name = 'content/data_pondok.html'


class Indikator1View(generic.TemplateView):
    template_name = 'content/indikator_1.html'

    def get_context_data(self, **kwargs):
        context_data = super(Indikator1View, self).get_context_data(**kwargs)
        # print(kwargs["pk"])
        context_data["data"] = pondok.objects.get(pk=kwargs['pk'])

        return context_data


class Indikator2View(generic.TemplateView):
    template_name = 'content/indikator_2.html'

    def get_context_data(self, **kwargs):
        context_data = super(Indikator2View, self).get_context_data(**kwargs)
        # print(kwargs["pk"])
        context_data["data"] = pondok.objects.get(pk=kwargs['pk'])

        return context_data


class Indikator3View(generic.TemplateView):
    template_name = 'content/indikator_3.html'

    def get_context_data(self, **kwargs):
        context_data = super(Indikator3View, self).get_context_data(**kwargs)
        # print(kwargs["pk"])
        context_data["data"] = pondok.objects.get(pk=kwargs['pk'])

        return context_data


class Indikator4View(generic.TemplateView):
    template_name = 'content/indikator_4.html'

    def get_context_data(self, **kwargs):
        context_data = super(Indikator4View, self).get_context_data(**kwargs)
        # print(kwargs["pk"])
        context_data["data"] = pondok.objects.get(pk=kwargs['pk'])

        return context_data


class Indikator5View(generic.TemplateView):
    template_name = 'content/indikator_5.html'

    def get_context_data(self, **kwargs):
        context_data = super(Indikator5View, self).get_context_data(**kwargs)
        # print(kwargs["pk"])
        context_data["data"] = pondok.objects.get(pk=kwargs['pk'])

        return context_data


class Indikator6View(generic.TemplateView):
    template_name = 'content/indikator_6.html'

    def get_context_data(self, **kwargs):
        context_data = super(Indikator6View, self).get_context_data(**kwargs)
        # print(kwargs["pk"])
        context_data["data"] = pondok.objects.get(pk=kwargs['pk'])

        return context_data


class Indikator7View(generic.TemplateView):
    template_name = 'content/indikator_7.html'

    def get_context_data(self, **kwargs):
        context_data = super(Indikator7View, self).get_context_data(**kwargs)
        # print(kwargs["pk"])
        context_data["data"] = pondok.objects.get(pk=kwargs['pk'])

        return context_data


class SelesaiView(generic.TemplateView):
    template_name = 'content/selesai.html'

    def get_context_data(self, **kwargs):
        context_data = super(SelesaiView, self).get_context_data(**kwargs)
        # print(kwargs["pk"])
        context_data["data"] = pondok.objects.get(pk=kwargs['pk'])

        return context_data


class EvaluasiView(generic.TemplateView):
    template_name = 'content/evaluasi.html'

    def get_context_data(self, **kwargs):
        context_data = super(EvaluasiView, self).get_context_data(**kwargs)
        context_data["data_pondok"] = pondok.objects.get(id=kwargs['pk'])
        context_data["data_indikator"] = ciri_ciri.objects.filter(
            indikator_id=pondok.objects.get(id=kwargs['pk']).status)

        return context_data


def get_evaluasi(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        status = request.POST.get('status')
        data_pondok = pondok.objects.get(id=id)
        data_pondok.status = status
        data_pondok.save()
        return JsonResponse({'message': 'Data sent successfully'})


def simpan_status(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        status = request.POST.get('status')
        print(id)
        print(status)

        data_pondok = pondok.objects.get(id=id)
        data_pondok.status = status
        data_pondok.save()
        return JsonResponse({'message': 'Data sent successfully'})


def get_indikator(request, pk):
    status = pondok.objects.get(pk=pk).status
    # print(status)
    match status:
        case 0:
            return redirect(reverse('ekonomi:indikator1', kwargs={'pk': pk}))
        case 1:
            return redirect(reverse('ekonomi:indikator2', kwargs={'pk': pk}))
        case 2:
            return redirect(reverse('ekonomi:indikator3', kwargs={'pk': pk}))
        case 3:
            return redirect(reverse('ekonomi:indikator4', kwargs={'pk': pk}))
        case 4:
            return redirect(reverse('ekonomi:indikator5', kwargs={'pk': pk}))
        case 5:
            return redirect(reverse('ekonomi:indikator6', kwargs={'pk': pk}))
        case 6:
            return redirect(reverse('ekonomi:indikator7', kwargs={'pk': pk}))
        case 7:
            return redirect(reverse('ekonomi:selesei', kwargs={'pk': pk}))
