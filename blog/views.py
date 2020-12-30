from django.shortcuts import render
from .models import Post

# Default mixins provided to authenicate Login required and User validation
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Importing default views for CRUD operations

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Post


# Create your views here.


def home(request):
    # What is context ?
    context = {
        'posts': Post.objects.all()
    }
    # render redirects to the blog home page
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

# class based views

# List view - outputs list based output views to generate outputs like lists
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    success_url = '/'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # if user is author, then only make changes
    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False

    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    success_url = '/'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False

