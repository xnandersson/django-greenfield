from rest_framework import serializers
from widget.models import Widget

class WidgetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Widget
        fields = ('id', 'display_name',)
