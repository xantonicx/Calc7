from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('blank5/', views.blank5, name='blank5'),
    path('blank6/', views.blank6, name='blank6'),
    path('blank7/', views.blank7, name='blank7'),
    path('blank8/', views.blank8, name='blank8'),
    path('blank9/', views.blank9, name='blank9'),
    path('blank10/', views.blank10, name='blank10'),
    path('blank11/', views.blank11, name='blank11'),
    path('blank12/', views.blank12, name='blank12'),
    path('blank13/', views.blank13, name='blank13'),
    path('blank14/', views.blank14, name='blank14'),
    path('blank15/', views.blank15, name='blank15'),
    path('yt_000001/', views.yt_000001, name='yt_000001'),
]