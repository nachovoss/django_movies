from rest_framework import serializers
from .models import Channel, ContentType, Lenguage, Metadata, Content, Group
from .service.channel_service import channel_service
from .service.content_service import content_sevrice
from rest_framework.response import Response


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("id", "name", "channels")
        extra_kwargs = {"channels": {"required": False}}


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = [
            "id",
            "title",
            "picture_url",
            "is_parent",
            "parent_channel",
            "date_created",
            "groups",
        ]
        extra_kwargs = {"groups": {"required": False}}

    def validate(self, data: dict) -> dict:
        id: int = self.context.get("view").kwargs.get("pk")

        """Check if parent channel is parent and if channel is parent"""
        parent_validation = channel_service.parent_channel_validation(
            id, data.get("is_parent"), data.get("parent_channel")
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

    def validate(self, data: dict) -> dict:
        """Check if channel exists"""

        channel_validation = content_sevrice.content_channel_validation(
            data.get("parent_channel").id
        )
        if isinstance(channel_validation, Response):
            return channel_validation
        return data

    def validate_rating(self, rating: int) -> int:
        """Check if rating is between 0 and 10"""
        rating_validation = content_sevrice.rating_validation(rating)
        if isinstance(rating_validation, Response):
            return rating_validation
        return rating
