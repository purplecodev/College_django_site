from django.urls import path
from .views import HomeNews, ViewNews # Импортируем представление для новостей

urlpatterns = [
    path('', HomeNews.as_view(), name='news'),
    path('news/<int:pk>/', ViewNews.as_view(), name='View_news'),
]
