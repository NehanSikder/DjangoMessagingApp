from django.conf.urls import url, include

from . import views


urlpatterns = [
	url(r'^$', views.MessagesListView.as_view(), name='index'),
    url(r'^message/(?P<pk>\d+)$', views.MessageDetailView.as_view(), name='message-detail'),
    url(r'^send/$', views.send_message, name='send_message'),


]