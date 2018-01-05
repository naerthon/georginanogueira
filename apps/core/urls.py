from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import index, galeria, contato, eventos,detail_eventos,detail_colecoes,detail_galeria

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^galeria/$', galeria, name='all-galeria'),
	url(r'^contato/$', contato, name='contato'),
	url(r'^eventos/$', eventos, name='all-eventos'),
	url(r'^colecoes/(?P<slug>[\w-]+)/$', detail_colecoes, name='detail-colecoes'),
	url(r'^galeria/(?P<slug>[\w-]+)/$', detail_galeria, name='detail-galeria'),
	url(r'^eventos/(?P<slug>[\w-]+)/$', detail_eventos, name='detail-eventos'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)