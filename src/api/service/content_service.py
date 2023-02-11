from ..models import Channel
from rest_framework import serializers


class ContentService:
    def __init__(self):
        pass

    def content_channel_validation(self, channel_id: int):
        """Check if channel exists"""
        channel = Channel.objects.filter(id=channel_id).first()
        if channel.is_parent:
            raise serializers.ValidationError(
                "Can't add content to a parent Channel"
            )
        return channel


content_sevrice = ContentService()
