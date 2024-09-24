from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('theme/', views.theme_list, name='theme_list'),  # Вывод тем и добавление темы
    path('theme/delete/<int:id>/', views.delete_theme, name='delete_theme'),  # Удаление темы
    path('notes/<int:theme_id>/', views.note_list, name='note_list'),  # Вывод заметок по теме и добавление заметки
    path('notes/delete/<int:id>/', views.delete_note, name='delete_note'),  # Удаление заметки
]
