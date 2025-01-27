from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.home, name='home'),
    path('start/', views.start_quiz, name='start_quiz'),
    path('score/', views.show_score, name='score'),
    path('finish/', views.finish_quiz, name='finish_quiz'),
]
