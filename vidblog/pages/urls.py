from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index', ),
    path('watch/<slug:slug>/', views.watch, name='watch'),
    path('category/<slug:slug>/', views.category_videos, name='category'),
 
]
