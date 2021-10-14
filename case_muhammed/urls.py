from django.contrib import admin
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from django.conf.urls import url

from django.views.static import serve
from core.views import token_view, create_form_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', token_view, name='control_token'),
    path('create-form/',create_form_view, name='create-form'),


    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
 


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)