from ..models import Channel
from rest_framework import serializers


class ContentService:
    def __init__(self):
        pass

    def content_channel_validation(self, channel_id: int) -> Channel:
        """Check if channel is parent"""
        channel = Channel.objects.filter(id=channel_id).first()
        if channel.is_parent:
            raise serializers.ValidationError(
                "Can't add content to a parent Channel"
            )
        return channel

    def rating_validation(self, rating: int) -> int:
        if rating < 0 or rating > 10:
            raise serializers.ValidationError(
                "Rating must be between 0 and 10"
            )
        return rating


content_sevrice = ContentService()
