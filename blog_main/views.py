from django.views.generic import ListView, DetailView
from blog_main.models import Post, Page
from django.shortcuts import redirect


class PostsListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


def contacts(request):
    page = Page.objects.get(id=1)
    return redirect(request, "pages/contacts.html", {"page": page})

