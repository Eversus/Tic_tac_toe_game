from django.urls import path
# Импортируем созданные нами представления
from .views import NewsList, NewsDetail, NewsCreate, NewsUpdate, ProductDelete

urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем новостям у нас останется пустым.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   # pk — это первичный ключ новости, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('', NewsList.as_view(), name='news_list'),
   path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
   path('news/create/', NewsCreate.as_view(), name='news_create'),
   path('articles/create/', NewsCreate.as_view(), name='articles_create'),
   path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='news_edit'),
   path('articles/<int:pk>/edit/', NewsUpdate.as_view(), name='articles_edit'),
   path('news/<int:pk>/delete/', ProductDelete.as_view(), name='news_delete'),
   path('articles/<int:pk>/delete/', ProductDelete.as_view(), name='articles_delete'),
]

