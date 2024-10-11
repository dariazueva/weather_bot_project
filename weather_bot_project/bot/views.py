from rest_framework import filters, viewsets

from .models import Log
from .serializers import LogSerializer


class LogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Log.objects.all().order_by("-timestamp")
    serializer_class = LogSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["user_id", "timestamp"]
