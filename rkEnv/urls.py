from django.urls import path
from . import views

urlpatterns=[
  path('',views.index,name='index'),
  path('count/', views.count, name='count'),
  path('register',views.register,name='register'),
  path('login',views.login,name='login'),
  path('logout',views.logout,name='logout'),
]