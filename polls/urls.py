from django.conf.urls import url

from . import views
from . import classviews

app_name='polls'
urlpatterns = [
    #url(r'^$',views.index,name='index'),
    #url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
    #url(r'^(?P<question_id>[0-9]+)/results/$',views.results,name='results'),
    #url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),

    url(r'^$', classviews.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', classviews.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', classviews.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', classviews.vote, name='vote'),
  ]