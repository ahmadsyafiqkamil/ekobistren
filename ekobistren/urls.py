from django.urls import path, re_path
from .views import *
from .ajax_datatable import PondokAjaxView, EvaluasiAjaxView

app_name = 'ekonomi'
urlpatterns = [
    path('daftar_pondok', DaftarPondok.as_view(), name='daftar_pondok'),
    path('', DataPondok.as_view(), name='data_pondok'),
    path('PondokAjaxView/', PondokAjaxView.as_view(), name='pondok_ajax_view'),
    path('EvaluasiAjaxView/', EvaluasiAjaxView.as_view(), name='EvaluasiAjaxView'),
    path('data_evaluasi/', DataEvaluasi.as_view(), name='data_evaluasi'),

    re_path('indikator1/(?P<pk>[-\w]*)$', Indikator1View.as_view(), name='indikator1'),
    re_path('indikator2/(?P<pk>[-\w]*)$', Indikator2View.as_view(), name='indikator2'),
    re_path('indikator3/(?P<pk>[-\w]*)$', Indikator3View.as_view(), name='indikator3'),
    re_path('indikator4/(?P<pk>[-\w]*)$', Indikator4View.as_view(), name='indikator4'),
    re_path('indikator5/(?P<pk>[-\w]*)$', Indikator5View.as_view(), name='indikator5'),
    re_path('indikator6/(?P<pk>[-\w]*)$', Indikator6View.as_view(), name='indikator6'),
    re_path('indikator7/(?P<pk>[-\w]*)$', Indikator7View.as_view(), name='indikator7'),
    re_path('selesai/(?P<pk>[-\w]*)$', SelesaiView.as_view(), name='selesei'),
    re_path('evaluasi/(?P<pk>[-\w]*)$', EvaluasiView.as_view(), name='evaluasi'),
    re_path('get_indikator/(?P<pk>[-\w]*)$', get_indikator, name='get_indikator'),
    path('detil_evaluasi/<pk>', DetilEvaluasi.as_view(), name='detil_evaluasi'),

    path('simpan_status/', simpan_status, name='simpan_status'),
    path('simpan_evaluasi/', simpan_evaluasi, name='simpan_evaluasi'),
    path('simpan_detil_evaluasi/', simpan_detil_evaluasi, name='simpan_detil_evaluasi'),

    # path('SuratAjaxView/', SuratAjaxView.as_view(), name='surat_ajax_view'),

    # path('notifications/', NotificationListView.as_view(), name='notifications'),
    # re_path('mark-as-read/(?P<slug>\d+)/$', mark_as_read, name='mark_as_read'),

]


