from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, View
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator
from .models import Post, Author, Category, PostCategory
from .filters import PostFilter
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.core.mail import send_mail, mail_managers
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from datetime import datetime
from pprint import pprint
from .filters import PostFilter
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, View
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator
from .models import Post, Author, Category, PostCategory
from .filters import PostFilter
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.dispatch import receiver, Signal

class NewsList(ListView):
    model = Post

    ordering = 'name'

    template_name = 'post.html'

    context_object_name = 'post'
# Create your views here.
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['time_now'] = datetime.utcnow()

        context['next_sale'] = 'Свежие новости кажду неделю!'
        pprint(context)
        return context


class NewsDetail(DetailView):
    model = Post

    template_name = 'one_post.html'

    context_object_name = 'post'


class Search(ListView):
  model = Post
  template_name = 'search.html'
  context_object_name = 'post_search'
  ordering = ['-dateCreation']
  filter_class = PostFilter # Для вывода фильтра не через форму
  paginate_by = 10

  def get_queryset(self):
    queryset = super().get_queryset()
    self.filter = self.filter_class(self.request.GET, queryset=queryset)
    return self.filter.qs.all()

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    # context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset()) # Если выводить фильтр только через формы
    context['filter'] = self.filter # Если выводить фильтр не через формы
    context['list_in_page'] = self.paginate_by # Для отображения кол-ва выведенных публикаций на странице
    context['all_posts'] = Post.objects.all() # Для отображения общего кол-ва публикаций на сайте
    return context


class CreatePost(PermissionRequiredMixin, CreateView):
    permission_required = ('main_app.add_post',)
    model = Post
    template_name = 'create_post.html'
    form_class = PostForm

    addpost = Signal()

    def form_valid(self, form):
        addpost = Signal()
        post = form.save()
        id = post.id
        a = form.cleaned_data['postCategory']
        category_object_name = str(a[0])
        # add_post_send_email.delay(category=category_object_name, id=id)
        addpost.send(Post, instance=post, category=category_object_name)
        return redirect(f'/news/{id}')


class EditPost(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
  permission_required = ('main_app.change_post',)
  template_name = 'post_edit.html'
  form_class = PostForm

  def get_object(self, **kwargs):
    id = self.kwargs.get('pk')
    return Post.objects.get(pk=id)




class DeletePost(LoginRequiredMixin, DeleteView):
  template_name = 'delete_post.html'
  queryset = Post.objects.all()
  success_url = '/news/'