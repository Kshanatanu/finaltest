"""noviz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from nvz.views import *
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('Admins/',Admins,name='Admins'),
    path('addfunc/',addfunc,name='addfunc'),
    path('allfunc/',allfunc,name='allfunc'),
    path('newfunc/',newfunc,name='newfunc'),
    path('final/',final,name='final'),
    path(r'^fdetails/(?<num>[0-9]+)$',fdetails,name='fdetails'),
    path(r'^sregister/(?<num>[0-9]+)',sregister,name='sregister'),
    path(r'^newdetails/(?<num>[0-9]+)$',newdetails,name='newdetails'),
    path(r'^sdetails/(?<num>[0-9]+)',sdetails,name='sdetails'),
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
