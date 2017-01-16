"""movie_rest_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from mrs.views import   MovieList, MovieDetail, RoleList, RoleDetail, PersonDetail, PersonList


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^persons/', PersonList.as_view(), name='person-list'),
    url(r'^person/(?P<pk>(\d)+)', PersonDetail.as_view(), name='person-detail'),
    url(r'^movies/', MovieList.as_view(), name='movie-list'),
    url(r'^movies/(?P<pk>(\d)+)', MovieDetail.as_view(), name='movie-detail'),
    url(r'^roles/(?P<pk>(\d)+)', RoleDetail.as_view(), name='role-detail'),
    url(r'^roles/', RoleList.as_view(), name='role-list'),
    
    
    

]
