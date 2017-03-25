from django.conf.urls import url

from . import views

app_name = 'memeconomy'
urlpatterns = [
	url(r'^profile$', views.profile, name='profile'),
	url(r'^create/$', views.create, name='create'),
	url(r'^(?P<meme_id>[0-9]+)/buy/$', views.buy, name='buy'),
	url(r'^(?P<meme_id>[0-9]+)/sell/$', views.sell, name='sell'),
	url(r'^(?P<meme_id>[0-9]+)/view/$', views.view, name='view'),
	url(r'^$', views.index, name='index')
]