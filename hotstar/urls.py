"""
URL configuration for hotstar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('registration/',registration,name='registration'),
    path('user_login/',user_login,name='user_login'),
    path('display_profile/',display_profile,name='display_profile'),
    path('user_logout/',user_logout,name='user_logout'),
    path('movies/',movies,name='movies'),
    path('change_password/',change_password,name='change_password'),
    path('reset_password/',reset_password,name='reset_password'),
    path('sports/',sports,name='sports')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

