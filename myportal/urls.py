from django.urls import path, include
from globus_portal_framework.urls import register_custom_index
from myportal.views import mysearch

register_custom_index('custom_search', ['schema-org-index'])


urlpatterns = [
    # Provides the basic search portal
    path('<custom_search:index>/', mysearch, name='search'),
    path('<custom_search:index>/', mysearch, name='detail'),

    path('', include('globus_portal_framework.urls')),
    path('', include('social_django.urls', namespace='social')),

]