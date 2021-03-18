from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('destory_session', views.destroy),
    path('count2', views.count2)
]