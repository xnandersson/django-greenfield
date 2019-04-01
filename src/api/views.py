from rest_framework import viewsets
from .serializers import WidgetSerializer
from widget.models import Widget

class WidgetViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows Widgets to be viewed or edited.
    """
    queryset = Widget.objects.all()
    serializer_class = WidgetSerializer

