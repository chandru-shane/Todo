from django.shortcuts import render
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
from .models import *

# Create your views here.


class TodoListView(ListView):
	template_name = 'app/index.html'
	model = Todo
	context_object_name = 'todos' 

class TodoCreateView(CreateView):
	model = Todo 
	fields = ['task','status']

class TodoDeleteView(DeleteView):
	model = Todo
	success_url = '/'

class TodoUpdateView(UpdateView):
	model = Todo
	template_name = 'app/update.html'
	fields = ['status']