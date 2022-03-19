from django import views
from django.urls import path,include
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.stud_login,name="login"),
    path('home',views.home,name="home"),
    path('notes',views.notes, name='notes'),
    path('delete_note/<int:pk>',views.delete_note, name='delete-note'),
    path('notes_detais/<int:pk>',views.NotesDetaisView.as_view(), name='notes_detais'),
    path('logout',views.stud_logout,name="logout")
    
]