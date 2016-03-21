
from django.conf.urls import url, patterns
from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    url(r'^$', 'qa.views.draw_new', name = 'new_questions'),
    url(r'^login/.*$', 'qa.views.test'),
    url(r'^signup/.*$','qa.views.test'),
    url(r'^question/(?P<q_id>\d+)/$','qa.views.draw_question', name = 'draw_question'),
    url(r'^ask/.*$','qa.views.test'),
    url(r'^popular/.*$','qa.views.draw_popular' name= 'draw_popular'),
    url(r'^new/.*$','qa.views.test')
]
