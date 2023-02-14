""""""
from ..models import Channel, Content
from rest_framework import serializers
from django.http import HttpResponse, Http404
from statistics import mean
import csv


class ChannelService:
    """Service for channel model"""

    def __init__(self):
        pass

    def parent_channel_validation(
        self, id: int, is_parent: bool, parent_channel: Channel
    ) -> Channel:
        """Check if parent channel is parent and if channel is parent"""

        if is_parent and parent_channel is not None:
            raise serializers.ValidationError(
                "Channel is parent and has a parent channel, this is not allowed"
            )
        if parent_channel is not None:
            if parent_channel.is_parent is False:
                raise serializers.ValidationError(
                    "selected  parent channel  can't be a aparent channel, this is not allowed"
                )
            if parent_channel.id == id:
                raise serializers.ValidationError(
                    "selected  parent channel  can't be the same as the channel, this is not allowed"
                )
        if not is_parent and parent_channel is None:
            check_for_childs = Channel.objects.filter(
                parent_channel=id
            ).first()
            if check_for_childs is not None:
                raise serializers.ValidationError(
                    "Channel has subchannels, can't set is_parent to False, this is not allowed"
                )

        return parent_channel

    def get_rating(self, channel_id: int) -> dict:
        """Get rating of channel"""

        channel = Channel.objects.filter(id=channel_id).first()

        if channel is None:
            raise Http404("Channel not found")

        if channel.is_parent:

            subchannels = Channel.objects.filter(parent_channel=channel.id)

            if subchannels.count() == 0:
                return {
                    "error": "Channel has no subchannels or contents",
                    "rating": 0,
                }
            ratings = []

            for subchannel in subchannels:
                contents = Content.objects.filter(parent_channel=subchannel.id)

                if contents.count() == 0:
                    continue

                ratings.append(mean([content.rating for content in contents]))

            return {
                "channel": channel.title,
                "rating": round(mean(ratings), 1),
            }

        contents = Content.objects.filter(parent_channel=channel.id)

        if contents.count() == 0:

            return {"error": "Channel has no contents", "rating": 0}

        ratings = mean([content.rating for content in contents])

        return {"channel": channel.title, "rating": ratings}

    def export_rattings_csv(self) -> HttpResponse:
        """Export ratings from all channels to csv"""

        channels = Channel.objects.all()
        if channels.count() == 0:
            return {"error": "There are no channels"}
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename=ratings.csv"

        writer = csv.writer(response)
        writer.writerow(["Channel Title", "Average Rating"])
        unsorted_channels = []

        for channel in channels:
            rating = self.get_rating(channel.id)
            unsorted_channels.append(
                [channel.title, round(rating.get("rating"), 1)]
            )

        for rating in sorted(
            unsorted_channels, key=lambda x: x[1], reverse=True
        ):
            writer.writerow(rating)

        return response

    def delete_parent_channel_if_no_subchannels(self, channel: Channel):
        """Delete parent channel if it has no subchannels"""
        if channel.is_parent:
            return
        subchannels = Channel.objects.filter(
            parent_channel=channel.parent_channel
        ).exclude(id=channel.id)
        if subchannels.count() == 0:
            channel.parent_channel.delete()


channel_service = ChannelService()
