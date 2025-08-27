"""
URL configuration for youtube project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users',views.USerViewSet)
router.register(r'groups',views.GroupViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.Home,name='home'),    
    path("about/",views.About,name='about'),
    path("post/",include('Dave.urls')),
    path("register/",include('register.urls')),
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)