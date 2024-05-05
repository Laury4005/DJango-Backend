from . import views
from django.urls import path

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('authors/', views.authors, name='authors'),
    path('api/authors/', views.author_list),
    path('api/authors/<int:pk>/', views.author_detail),
]