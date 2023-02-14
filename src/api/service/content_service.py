from ..models import Channel, Content
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

    def delete_channel_if_no_contents(self, content: Content):
        """Delete channel if no contents and no subchannels"""
        content_channel = content.parent_channel
        contents = Content.objects.filter(
            parent_channel=content_channel.id
        ).exclude(id=content.id)
        if content_channel.is_parent:

            parent_channel = content_channel.parent_channel
            other_subchannels = Channel.objects.filter(
                parent_channel=parent_channel.id
            ).exclude(id=content_channel.id)
            if other_subchannels.count() == 0:
                parent_channel.delete()

        if contents.count() == 0 and content_channel.is_parent is False:
            content_channel.delete()


content_sevrice = ContentService()
