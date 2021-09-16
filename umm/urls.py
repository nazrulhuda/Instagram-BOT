from . import views
from django.urls import path

urlpatterns=[

    path('', views.blog, name='ji'),
    path('sagol/', views.sagol, name='jina'),
    path('phone/', views.tika, name='right'),
    path('thik/',views.pada, name='thikthak'),




 ]
