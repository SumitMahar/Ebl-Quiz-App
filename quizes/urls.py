from django.urls import path, include

from .views import (
    QuizListView,
    quiz_view,
    quiz_data_view,
    save_quiz_view,
    about_view
)

app_name = 'quizes'

urlpatterns = [
    path('', about_view, name='quiz_home' ),
    path('about/', about_view, name='about'),
    path('quiz/<pk>/', quiz_view, name='quiz_view' ),
    path('quiz/<pk>/data/', quiz_data_view, name='quiz_data_view'),
    path('quiz/<pk>/save', save_quiz_view, name='quiz_save_view' ),

]
  