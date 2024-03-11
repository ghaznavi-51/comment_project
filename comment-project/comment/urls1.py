from django.urls import path
from .import views


urlpatterns = [
    path('home/', views.home,name="home"),
    path('comment/', views.comment,name="comment"),
    path('data/', views.data,name="data"),
    path('datatable/', views.datatable,name="datatable"),
]

'''from django.urls import path
from . import views
urlpatterns = [
    path('', views.comment, name='comment'),
    path('data/', views.data, name='data'),
    path('datatable/', views.datatable, name='datatable'),
    path('saveData/', views.saveData, name='saveData')
]'''