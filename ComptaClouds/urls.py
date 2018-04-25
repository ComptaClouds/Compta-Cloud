# djauth/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('compte/', TemplateView.as_view(template_name='home.html'), name='home'),

    path('users/', include('comptaApp.urls')),
    #path('users/', include('django.contrib.auth.urls')),
]