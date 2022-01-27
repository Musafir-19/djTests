from django.views.generic import ListView
from blog.views import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


