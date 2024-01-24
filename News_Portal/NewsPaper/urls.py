from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    # Делаем так, чтобы все адреса из нашего приложения (NewsPaper/urls.py)
    # подключались к главному приложению с префиксом all-posts/.
    path('all-posts/', include('news.urls')),
    path('', include('protect.urls')),
    path('sign/', include('sign.urls')),
    path('accounts/', include('allauth.urls')),
]