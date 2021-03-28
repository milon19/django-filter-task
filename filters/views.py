import datetime
import json
from django.db.models import Q
from django.views.generic import View
from django.http import JsonResponse
from django.db import connection

from filters.models import SearchHistory


class SearchHistoryListView(View):
    @staticmethod
    def date_time_query(time):
        if time == 'Y':
            return Q(search_time__date=datetime.date.today() - datetime.timedelta(days=1))
        elif time == 'W':
            return Q(search_time__gte=datetime.date.today() - datetime.timedelta(weeks=1))
        else:
            return Q(search_time__gte=datetime.date.today() - datetime.timedelta(days=30))

    def get(self, request, *args, **kwargs):
        qs_users = request.GET.getlist('username')
        qs_keywords = request.GET.getlist('keyword')
        time = request.GET.get('time', None)

        search_history = SearchHistory.objects.select_related('user').all()

        if qs_users:
            if 'None' in qs_users:
                search_history = search_history.filter(Q(user=None) | Q(user__username__in=qs_users))
            else:
                search_history = search_history.filter(user__username__in=qs_users)

        if qs_keywords:
            search_history = search_history.filter(keyword__in=qs_keywords)

        if time:
            time_qs = self.date_time_query(time)
            search_history = search_history.filter(time_qs)

        search_history = list(search_history)
        search_history_data = [
            {
                'user': x.user.username if x.user else None,
                'keyword': x.keyword,
                'time': str(x.search_time)
            }
            for x in search_history
        ]
        print(len(connection.queries))
        return JsonResponse(json.dumps(search_history_data), safe=False)
