from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users', views.search_user, name='users'),
    path('hash', views.search_diplom_by_hash, name='hash'),
    path('create_hash', views.hash_file, name='create_hash'),
    path('blockchain_hash', views.view_hash_blockchain, name='search_hash'),
]