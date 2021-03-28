from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('', include('users.urls', namespace='users')),
    path('', include('posts.urls', namespace='posts')),
    path('', include('filters.urls', namespace='filters')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
