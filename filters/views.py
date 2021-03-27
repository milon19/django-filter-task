import json
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.views.generic import View
from django.http import JsonResponse
from django.db import connection

from filters.models import SearchHistory


class SearchHistoryListView(View):
    def get(self, request, *args, **kwargs):
        search_history = SearchHistory.objects.select_related('user').all()
        search_history=list(search_history)
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
