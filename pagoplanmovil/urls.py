from django.conf.urls import url
from . import views



#para llamar a nuestra página para insertar tenemos que invocar la dirección /pelicula/nueva

# se puede crear un hipervinculo para llamarla, en este ejemplo hay que invocar manualmente la dirección.

urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    #url(r'^pelicula/nueva/$', views.pelicula_nueva, name='pelicula_nueva'),
    url(r'^cliente/new/$', views.cliente_new, name='cliente_new'),
    url(r'^$', views.cliente_list, name='cliente_list'),
    url(r'^cliente/(?P<pk>[0-9]+)/$', views.cliente_detail,  name='cliente_detail'),
    url(r'^cliente/new/$', views.cliente_new, name='cliente_new'),
    url(r'^cliente/(?P<pk>[0-9]+)/edit/$', views.cliente_edit, name='cliente_edit'),
    url(r'^cliente/(?P<pk>\d+)/remove/$', views.cliente_remove, name='cliente_remove'),
    
    url(r'^combo/$', views.combo_list, name='combo_list'),
    url(r'^combo/(?P<pk>[0-9]+)/$', views.combo_detail,  name='combo_detail'),
    url(r'^combo/new/$', views.combo_new, name='combo_new'),
    url(r'^combo/(?P<pk>[0-9]+)/edit/$', views.combo_edit, name='combo_edit'),
    url(r'^combo/(?P<pk>\d+)/remove/$', views.combo_remove, name='combo_remove'),

    url(r'^pago/$', views.pago_list, name='pago_list'),
    url(r'^pago/new/$', views.pago_new, name='pago_new'),

    url(r'^factura/$', views.factura_list, name='factura_list'),
    ]