from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'),
    path('kom', views.kom, name='kom'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='NewsDetailView'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='NewsUpdateView'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='NewsDeleteView')
]
