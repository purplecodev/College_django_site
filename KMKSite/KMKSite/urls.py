from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Главная страница
    path('news/', include('news.urls')),  # Подключаем маршруты приложения 'news'
    path('informatics/', views.informatics_detail, name='informatics_detail'),
    path('medicine/', views.medicine_detail, name='medicine_detail'),
    path('economics/', views.economics_detail, name='economics_detail'),
    path('auth/', include('authentication.urls')),  # Подключаем маршруты приложения 'authentication'
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
