from django.urls import path
from .views import UserUpdateView, UserCreateView, UserDeleteView, UserDetailView, UserListView

urlpatterns = [
    path('usermodel/', UserListView.as_view(), name='user_list'),
    path('usermodel/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('usermodel/new/', UserCreateView.as_view(), name='user_create'),
    path('usermodel/<int:pk>/edit/', UserUpdateView.as_view(), name='user_edit'),
    path('usermodel/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
]