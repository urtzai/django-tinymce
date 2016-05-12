# Copyright (c) 2008 Joost Cassee
# Licensed under the terms of the MIT License (see LICENSE.txt)
from django.conf.urls import url
from django.views.generic import TemplateView

from tinymce import views


urlpatterns = [
    url(r'^js/textareas/(?P<name>.+)/$', views.textareas_js,
        name='tinymce-js'),
    url(r'^js/textareas/(?P<name>.+)/(?P<lang>.*)$', views.textareas_js,
        name='tinymce-js-lang'),
    url(r'^ajax/photologue/upload$', views.upload_photologue, name='upload_photologue'),
    url(r'^ajax/photologue/get_photos$', views.get_photologue, name='get_photologue'),
    url(r'^spellchecker/$', views.spell_check),
    url(r'^flatpages_link_list/$', views.flatpages_link_list),
    url(r'^compressor/$', views.compressor, name='tinymce-compressor'),
    url(r'^filebrowser/$', views.filebrowser, name='tinymce-filebrowser'),
    url(r'^photologue.js$', views.photologue, name='tinymce-photologue'),
    url(r'^preview/(?P<name>.+)/$', views.preview, name='tinymce-preview'),
    url(r'^photologue/panel$', TemplateView.as_view(template_name='templates/photologue/index.html'), name="home"),
]
