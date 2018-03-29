from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.news, name='news'),
    path('hot/', views.hot, name='hot'),
    path('best/', views.best, name='best'),
    path('<int:post_id>/', views.results, name='results')
]