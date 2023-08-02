
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
import notifications.urls
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('ekobistren.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('inbox/notifications/', include(notifications.urls, namespace='notifications'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)