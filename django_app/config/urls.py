"""config URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin

from main import views as main_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main_views.index, name='index'),

    # 아래 signup url을 직접 셋팅 할 경우 1단계 에서 진행한 로그인이 풀려버림
    # url(r'accounts/social/signup/', main_views.main, name='redirect_main'),

    url(r'^accounts/', include('allauth.urls')),
    url(r'^main/', include('main.urls')),
]
