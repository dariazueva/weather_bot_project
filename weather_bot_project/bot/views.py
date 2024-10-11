from rest_framework import viewsets, filters

from .models import Log
from .serializers import LogSerializer


class LogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Log.objects.all().order_by("-timestamp")
    serializer_class = LogSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, filters.BaseFilterBackend]
    filterset_fileds = ['user_id', 'timestamp']
