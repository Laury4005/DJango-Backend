from . import views
from django.views.generic import TemplateView
from django.urls import path

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='login.html'), name='home'),
    path('accounts/login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('authors/', views.authors, name='authors'),
    path('api/authors/', views.author_list, name="author_list"),
    path('api/authors/<int:pk>/', views.author_detail, name='author_detail'),
]