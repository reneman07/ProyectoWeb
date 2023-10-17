from django.urls import path, include, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('', views.blog, name = 'Blog'),
    path('categoria/<categoria_id>/', views.categoria, name = 'categoria'),
    
]

