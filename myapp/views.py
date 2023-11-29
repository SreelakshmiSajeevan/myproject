from django.shortcuts import render,  get_list_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import User
from .forms import UserForm


class UserListView(ListView):
    model = User
    template_name = 'myapp/user_list.html'
    context_object_name = 'user_list'

class UserDetailView(DetailView):
    model = User
    template_name = 'myapp/user_detail.html'
    context_object_name = 'User'

class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'myapp/user_form.html'
    success_url = reverse_lazy('user_list')

class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'myapp/user_form.html'
    success_url = reverse_lazy('user_list')

class UserDeleteView(DeleteView):
    model = User
    template_name = 'myapp/user_delete.html'
    success_url = reverse_lazy('user_list')
