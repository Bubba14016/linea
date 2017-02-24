from django.conf.urls import url
from apps.publicacion.views import Listar


urlpatterns = [
	url(r'^listar$',Listar.as_view(), name='listar'),

   
]