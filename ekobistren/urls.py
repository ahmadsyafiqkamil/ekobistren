from django.urls import path, re_path
from .views import *
from .ajax_datatable import PondokAjaxView

app_name = 'ekonomi'
urlpatterns = [
    path('daftar_pondok', DaftarPondok.as_view(), name='daftar_pondok'),
    path('', DataPondok.as_view(), name='data_pondok'),
    path('PondokAjaxView/', PondokAjaxView.as_view(), name='pondok_ajax_view'),

    # path('indikator1', Indikator1View.as_view(), name='indikator1'),
    path('indikator2', Indikator2View.as_view(), name='indikator2'),
    path('indikator3', Indikator3View.as_view(), name='indikator3'),
    path('indikator4', Indikator4View.as_view(), name='indikator4'),
    path('indikator5', Indikator5View.as_view(), name='indikator5'),
    path('indikator6', Indikator6View.as_view(), name='indikator6'),
    path('indikator7', Indikator7View.as_view(), name='indikator7'),

    re_path('indikator1/(?P<pk>[-\w]*)$', Indikator1View.as_view(), name='indikator1'),

    # path('SuratAjaxView/', SuratAjaxView.as_view(), name='surat_ajax_view'),

    # path('notifications/', NotificationListView.as_view(), name='notifications'),
    # re_path('mark-as-read/(?P<slug>\d+)/$', mark_as_read, name='mark_as_read'),

]
