from django.urls import path
from . import views

urlpatterns = [
    path('add_note/', views.Add_Note, name='add-note'),
    path('', views.list_notes, name='list-note'),
    path('upadte_notes/<int:pk>/', views.update_note, name='update-note'),
    path('delete/<int:pk>/', views.delete_note, name='delete-note'),
    path('category/add/', views.add_category, name='add-category'),
    path('category/update/<int:pk>/', views.update_category, name='update-category'),
    path('category/list', views.list_category, name='list-category'),
    path('category/delete/<int:pk>/', views.delete_category, name='delete-category'),
    path('category/notes_by_category/<int:pk>/', views.notes_by_category, name='notes-by-category'),
]
