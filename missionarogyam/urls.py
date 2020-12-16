"""missionarogyam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static

urlpatterns = [
path('admin/', admin.site.urls),
path('',include('arogyam.urls')),
url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
path('kidneycare/', include('kidneycare.urls')),
path('heartcare/', include('heartcare.urls')),
path('diabetescare/', include('diabetescare.urls')),
path('cancercare/', include('cancercare.urls')),
path('immunitybooster/', include('immunitybooster.urls')),
path('arogyaveda/', include('arogyaveda.urls')),
path('muscleveda/', include('muscleveda.urls')),
path('nutriveda/', include('nutriveda.urls')),
path('rupam/', include('rupam.urls')),

]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
