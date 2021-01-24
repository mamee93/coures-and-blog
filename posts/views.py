from django.shortcuts import render
from django.views.generic import  DetailView, ListView
from .models import Post,Gategory,Author
from django.db.models import Count
from django.db.models import Q
from taggit.models import Tag
# Create your views here.

 

def index(request):
    
    return render(request, 'index.html', {})

class BlogListView(ListView):
    model = Post
 
    paginate_by = 10
    def get_queryset(self):
        name = self.request.GET.get('q','')
        object_list = Post.objects.filter(
            Q(title__icontains=name)|
            Q(overview__icontains=name)
		)
        return object_list
    template_name = 'post/blog.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_post'] = Post.objects.all()[:3]
        context['categories'] = Gategory.objects.all().annotate(post_count=Count("post_category"))
         
        return context
    

class PostDetailView(DetailView):
    model = Post
    
    template_name = 'post/blog-detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Gategory.objects.all()
        context['tags'] =  Tag.objects.all()
        context['Author'] =  Author.objects.all()
        return context
    
    