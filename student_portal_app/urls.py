from django import views
from django.urls import path,include
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.login,name="login"),
    path('userhome',views.userhome,name="userhome"),
    path('adminhome',views.adminhome,name="adminhome"),
    path('logout',views.logout,name="logout"),
    path('createuser',views.createuser,name="createuser"),
    path('delete_stud/<int:pk>',views.delete_stud, name='delete-stud'),
    path('update_stud/<int:pk>',views.update_stud, name='update-stud'),
    path('update_stud_details/<int:pk>',views.update_stud_details, name='update_stud_details'),
    
]