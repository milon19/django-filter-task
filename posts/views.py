from django.db.models import Q
from django.views.generic import ListView

from posts.models import Post
from filters.models import SearchHistory


class PostListView(ListView):
    template_name = 'posts/post_list.html'
    model = Post
    context_object_name = 'posts'


class PostSearchView(ListView):
    template_name = 'posts/post_search.html'
    context_object_name = 'posts'

    def get_context_data(self, *args, **kwargs):
        context = super(PostSearchView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        if query is None:
            query = ''
        context['query'] = query
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query and query != '':
            lookups = Q(title__icontains=query) | Q(body__icontains=query)
            queryset = Post.objects.filter(lookups)
            search_data = {
                'user': request.user if request.user.is_authenticated else None,
                'keyword': query
            }
            SearchHistory.objects.create(**search_data)
            return queryset
        else:
            return Post.objects.all()
