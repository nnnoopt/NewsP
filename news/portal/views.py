from django.views.generic import ListView, DetailView
from .models import *
from datetime import datetime


class PostList(ListView):
    model = Post

    ordering = '-create_at'

    template_name = 'posts.html'

    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['time_now'] = datetime.utcnow()

        context['next_sale'] = None
        return context


class PostDetail(DetailView):
    model = Post

    template_name = 'postdetail.html'

    context_object_name = 'post'
