from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginpage, name='login'),
    path('logout', views.logoutpage, name='logout'),
    path('createaccount', views.createaccount, name='createaccount'),
    path('course/<str:cid>/', views.singleCourseView, name='courseview'),
]
