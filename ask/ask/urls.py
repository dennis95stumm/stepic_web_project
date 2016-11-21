from django.conf.urls import patterns, include, url

from django.contrib import admin
from qa.views import test, question_details, question_list_main
admin.autodiscover()

urlpatterns = patterns('qa.views',
  # Examples:
  # url(r'^$', 'ask.views.home', name='home'),
  # url(r'^blog/', include('blog.urls')),

  url(r'^admin/', include(admin.site.urls)),
  url(r'^.*$', question_list_main, name='index'),
  url(r'^login/$', test, name='login'),
  url(r'^signup/$', test, name='signup'),
  url(r'^question/(?P<id>[0-9]+)/$', question_details, name='question'),
  url(r'^ask/.*$', test, name='ask'),
  url(r'^popular/.*$', question_list_main, name='popular'),
  url(r'^new/$', test, name='new'),
)
