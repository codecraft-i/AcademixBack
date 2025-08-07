from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = "__all__"

    def get_image_url(self, obj):
        request = self.context.get("request")
        if obj.image:
            url = obj.image.url
            return request.build_absolute_uri(url) if request else url
        return None
