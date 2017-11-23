from django.conf.urls import url, include
from django.contrib import admin
from apps.core import urls as core_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(core_urls, namespace='core')),
]
