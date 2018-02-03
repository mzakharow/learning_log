from django.conf.urls import url

from . import views

app_name ='learning_logs'

urlpatterns = [
    url(r'^$', views.index, name='index'),

    #List
    url(r'^topics/$', views.topics, name='topics'),

    #single
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    #page for newtopic
    url(r'^new_topic/$', views.new_topic, name='new_topic'),

    #page for new entry
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    #page for edit entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]