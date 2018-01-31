from django.conf.urls import url

from . import views

app_name ='learning_logs'

urlpatterns = [
    url(r'^$', views.index, name='index'),

    #List
    url(r'^topics/$', views.topics, name='topics'),

    #single
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]