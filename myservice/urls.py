from django.urls import path
from . import views
urlpatterns = [
    path('myservice/', views.myservice, name='myservice'),
    path('interior/', views.interior, name='interior'),
    path('architectural/', views.architectural, name='architectural'),
    path('visu/', views.visu, name='visu'),
    path('project/', views.project, name='project'),
    path('product/', views.product, name='product'),
]