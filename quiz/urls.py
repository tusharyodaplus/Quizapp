"""quizapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from quizapp.views import user_login,user_logout,success
from django.urls import path
from django.contrib import admin
from django.views.generic import RedirectView
from rest_framework.urlpatterns import format_suffix_patterns
from quizapp import views

urlpatterns = [
    path('', user_login, name="user_login"),
    path('success/', success, name="user_success"),
    path('logout/', user_logout, name="user_logout"),
    url(r'^$', include('quizapp.urls')),
    url(r'^home/', include('quizapp.urls')),
    url(r'^quizlovers/', views.quizList.as_view()),
    url(r'^quiz/', include('quizapp.urls')),
    url(r'^admin/', admin.site.urls),
]
