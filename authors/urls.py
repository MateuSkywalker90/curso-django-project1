from django.urls import path

from . import views

app_name = 'authors'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('resgiter/create/', views.register_create, name='create'),
]
