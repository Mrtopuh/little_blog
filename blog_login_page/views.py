from django.views.generic import ListView, DetailView
from blog_login_page.models import Post
from django.http import HttpResponse


class PostsListView(ListView):  # представление в виде списка
    model = Post                   # модель для представления


class PostDetailView(DetailView):  # детализированное представление модели
    model = Post

