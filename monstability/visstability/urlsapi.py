from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import viewsapi

URL_FORMAT_OVERRIDE = 'params'

urlpatterns = format_suffix_patterns([
    path('nodes/', viewsapi.NodesViewSet.as_view({'get': 'list', 'post': 'create',})),
    path('nodes/<int:pk>/', viewsapi.NodesViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy',})),
    path('edges/', viewsapi.EdgesViewSet.as_view({'get': 'list', 'post': 'create',})),
    path('edges/<int:pk>/', viewsapi.EdgesViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy',})),
])
