from django.urls import path, include
from .views import *

# router = DefaultRouter()
# router.register(r'snippets', SnippetViewSet)
# router.register(r'tags', TagViewSet)

urlpatterns = [
    path('overview/', OverviewAPI.as_view(), name='overview-api'),
]
