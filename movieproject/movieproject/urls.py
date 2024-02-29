"""
URL configuration for movieproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from movie import views

app_name='movie'

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    # path("",views.viewmovie,name='viewmovie'),
    path('',views.MovieList.as_view(),name='viewmovie'),
    # path('addmovie',views.addmovie,name='addmovie'),
    path('addmovie',views.MovieAdd.as_view(),name='addmovie'),
    # path('detail/<p>',views.detail,name='detail'),
    path("detail/<pk>",views.MovieDetail.as_view(),name='detail'),
    # path('delete/<p>',views.delete,name='delete'),
    path('delete/<pk>',views.MovieDelete.as_view(),name='delete'),
    # path('update/<p>',views.update,name='update'),
    path('update/<pk>',views.MovieUpdate.as_view(),name='update'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)