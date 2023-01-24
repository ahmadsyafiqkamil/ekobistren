from django.urls import path, re_path
from .views import *

app_name = 'ekonomi'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('indikator1', Indikator1View.as_view(), name='indikator1'),
    path('indikator2', Indikator2View.as_view(), name='indikator2'),
    path('indikator3', Indikator3View.as_view(), name='indikator3'),

    # path('notifications/', NotificationListView.as_view(), name='notifications'),
    # re_path('mark-as-read/(?P<slug>\d+)/$', mark_as_read, name='mark_as_read'),

]
