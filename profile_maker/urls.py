from django.urls import path
from . import views
from django_playground import settings
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.create_profile, name = 'create'),
    path('list', views.list_view),
    path('<id>', views.detail_view),
    path('<id>/update', views.update_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)