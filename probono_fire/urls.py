"""probono_fire URL Configuration

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
from distributed import fire_and_forget
from django.contrib import admin
from django.urls import path,include

#이미지 url 
from django.conf.urls.static import static
from django.conf import settings

from probono_fire.views import front_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('appaccount.urls')),
    path('',front_page,name='front'),
    path('fire/',include('fire_situation.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)