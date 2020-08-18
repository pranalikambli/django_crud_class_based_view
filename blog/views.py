from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Blogs
from .forms import BlogForm


class IndexView(ListView):
    model = Blogs
    queryset = Blogs.objects.filter(status='published').all(). \
        order_by('-published_at')
    template_name = 'blog/list_view.html'
    context_object_name = 'index_post_list'


class DetailedView(DetailView):
    model = Blogs
    template_name = 'blog/detail_view.html'
    context_object_name = 'post'


class ManagePostList(ListView):
    model = Blogs
    template_name = 'blog/manage_post_list.html'
    context_object_name = 'manage_post_list'


class AddView(CreateView):
    model = Blogs
    form_class = BlogForm
    template_name = 'blog/add_view.html'
    success_url = '/'



class EditView(UpdateView):
    model = Blogs
    form_class = BlogForm
    pk_url_kwarg = 'pk'
    template_name = 'blog/edit_view.html'
    success_url = '/blog/manage_post_list'


class DeletePostView(DeleteView):
    model = Blogs
    pk_url_kwarg = 'pk'
    template_name = 'blog/delete_view.html'
    success_url = '/blog/manage_post_list'