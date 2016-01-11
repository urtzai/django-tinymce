# Copyright (c) 2008 Joost Cassee
# Licensed under the terms of the MIT License (see LICENSE.txt)

try:
    from django.conf.urls import url, patterns
except:
    from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('tinymce.views',
    url(r'^js/textareas/(?P<name>.+)/$', 'textareas_js', name='tinymce-js'),
    url(r'^js/textareas/(?P<name>.+)/(?P<lang>.*)$', 'textareas_js', name='tinymce-js-lang'),
    url(r'^ajax/photologue/upload$', 'upload_photologue', name='upload_photologue'),
    url(r'^ajax/photologue/get_photos$', 'get_photologue', name='get_photologue'),
    url(r'^spellchecker/$', 'spell_check'),
    url(r'^flatpages_link_list/$', 'flatpages_link_list'),
    url(r'^compressor/$', 'compressor', name='tinymce-compressor'),
    url(r'^filebrowser/$', 'filebrowser', name='tinymce-filebrowser'),
   	url(r'^photologue.js$', 'photologue', name='tinymce-photologue'),
    url(r'^preview/(?P<name>.+)/$', 'preview', name='tinymce-preview'),
)
