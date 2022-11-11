from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls,name = 'admin'),
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('pricing', views.pricing, name='pricing'),
    path('login',views.login,name = 'login'),
    path('logout', views.logout, name='logout'),
    path('forgot', views.forgot, name='forgot'),
    path('logged', views.logged, name='logged'),
    path('register', views.register, name='register'),
    path('createtask', views.createtask, name='createtask'),
    path('viewtask', views.viewtask, name='viewtask'),
    path('updatetask/<str:pk>/', views.updatetask, name='updatetask'),
    path('deletetask/<str:pk>/', views.deletetask, name='deletetask'),
]
