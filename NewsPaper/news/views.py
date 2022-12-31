from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filters import PostFilter
from .forms import PostForm



class PostsList(ListView):
    model = Post
    ordering = 'title'
    ordering = '-dateCreation'
    template_name = 'flatpages/posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'flatpages/post.html'
    context_object_name = 'post'


class PostSearch(ListView):
    model = Post
    ordering = 'title'
    ordering = '-dateCreation'
    template_name = 'flatpages/search.html'
    context_object_name = 'search'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class SearchDetail(DetailView):
    model = Post
    template_name = 'flatpages/post.html'
    context_object_name = 'post'


class PostDelete(DeleteView):
    model = Post
    template_name = 'flatpages/delete.html'
    success_url = '/posts/'


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'flatpages/edit.html'
    success_url = '/posts/'


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'flatpages/create.html'
    success_url = '/posts/'
