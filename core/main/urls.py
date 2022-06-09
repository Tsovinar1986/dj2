from django.urls import path
from .views import CategoryView, CategoryDetail,HomeView,register_request,login_request,logout_request,AddPostListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<str:cats>/', CategoryView.as_view(), name='category'),
    path('category/<int:id>', CategoryDetail.as_view(), name='category_detail'),
    path('register', register_request, name='register'),
    path('login', login_request, name='login'),
    path('logout',logout_request, name = 'logout'),
    path('add_post', AddPostListView.as_view(), name='add_post'),
    ]
