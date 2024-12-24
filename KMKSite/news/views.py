from .models import News
from django.views.generic import ListView, DetailView

class HomeNews(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'News/news.html'
    extra_context = {'title': 'Новости'}
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новости колледжа'
        return context

class ViewNews(DetailView):
    model = News
    template_name = 'News/news_detail.html'
    context_object_name = 'news_item'
