from datetime import date

from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField
from .models import Post


class NewsForm(ModelForm):
    title = CharField(label='Название')
    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'author',
            'categories',
        ]

        labels = {
            'author': 'Автор',
            'text': 'Текст',
            'categories': 'Категория'
        }

    def clean(self):
        cleaned_data = super().clean()
        author = cleaned_data.get('author')
        today = date.today()
        post_limit = Post.objects.filter(author=author, time_in__date=today).count()
        if post_limit >= 3:
            raise ValidationError('Нельзя публиковать больше 3 постов в сутки!')
        return cleaned_data