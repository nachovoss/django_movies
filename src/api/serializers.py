from rest_framework import serializers
from .models import Channel, ContentType, Lenguage, Metadata, Content
from .service.channel_service import channel_service
from .service.content_service import content_sevrice
from rest_framework.response import Response


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = "__all__"

    def validate(self, data: dict):
        """Check if parent channel is parent and if channel is parent"""
        parent_validation = channel_service.parent_channel_validation(
            data.get("is_parent"), data.get("parent_channel")
        )
        if isinstance(parent_validation, Response):
            return parent_validation
        return data


class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = "__all__"


class LenguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lenguage
        fields = "__all__"


class MetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metadata
        fields = "__all__"


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = "__all__"

    def validate(self, data: dict):
        """Check if channel exists"""

        channel_validation = content_sevrice.content_channel_validation(
            data.get("parent_channel").id
        )
        if isinstance(channel_validation, Response):
            return channel_validation
        return data