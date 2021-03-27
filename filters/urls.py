from django.urls import path

from filters.views import SearchHistoryListView

app_name = 'filters'

urlpatterns = [
    path('search-history/', SearchHistoryListView.as_view(), name='search-history'),
]
