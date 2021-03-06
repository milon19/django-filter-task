from django.db.models import Count
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model

from filters.models import SearchHistory

User = get_user_model()


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomePageView, self).get_context_data(*args, **kwargs)
        users = User.objects.all()
        keywords = SearchHistory.objects.all().values('keyword').annotate(count=Count('keyword')).order_by('keyword')
        time = SearchHistory.objects.values('search_time')

        context['users'] = users

        context['keywords'] = keywords
        context['time'] = {a['search_time'] for a in time}

        return context