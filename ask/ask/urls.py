from django.conf.urls import patterns, include, url

from django.contrib import admin
from qa.views import test, question_details, question_list_main, answer_add, question_add, sign_up, login
from django.contrib.auth import views as auth_views

admin.autodiscover()

urlpatterns = patterns('qa.views',
  # Examples:
  # url(r'^$', 'ask.views.home', name='home'),
  # url(r'^blog/', include('blog.urls')),

  url(r'^admin/', include(admin.site.urls)),
  url(r'^$', question_list_main, name='index'),
  url(r'^login/$', auth_views.login, { 'template_name': 'qa/login.html' }),
  url(r'^signup/$', sign_up, name='signup'),
  url(r'^question/(?P<id>[0-9]+)/$', question_details, name='question'),
  url(r'^answer/$', answer_add, name='answer'),
  url(r'^ask/$', question_add, name='ask'),
  url(r'^popular/$', question_list_main, name='popular'),
  url(r'^new/$', test, name='new'),
)
