from django.urls import path
from . import views
app_name="posts"
urlpatterns = [
    path('', views.index,name="index"),
    path('blog', views.BlogListView.as_view(),name='blog-list'),
    path('<str:slug>', views.PostDetailView.as_view(),name='post-detail'),
    #path('search', views.search,name="search"),
    #path('create', views.post_create ,name="post-create"),
    #path('post/<int:id>/', views.post,name="post-detail"),
    #path('post/<int:id>/update', views.post_update ,name="post-update"),
    #path('post/<int:id>/delete', views.post_delete ,name="post-delete"),

]
