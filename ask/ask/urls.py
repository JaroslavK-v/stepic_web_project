
from django.conf.urls import url, patterns
from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    url(r'^$', 'qa.views.draw_new', name = 'new_questions'),
    url(r'^login/.*$', 'qa.views.test'),
    url(r'^signup/.*$','qa.views.test'),
    url(r'^question/(?P<id>\d+)/$','qa.views.draw_question', name = 'draw_question'),
    url(r'^ask/.*$','qa.views1.test'),
    url(r'^popular/.*$','qa.views.draw_popular' name= 'draw_popular'),
    url(r'^new/.*$','qa.views.test')
]
