from django.urls import path
from . import views

urlpatterns = [
				path('',views.TodoListView.as_view(),name='index'),
				path('create/',views.TodoCreateView.as_view(),name='create'),
				path('<int:pk>/update/',views.TodoUpdateView.as_view(),name='update'),
				path('<int:pk>/delete/',views.TodoDeleteView.as_view(),name='delete'),
				]