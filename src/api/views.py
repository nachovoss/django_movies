""" Views for the Immfly API. """
from django.db.models import QuerySet
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Channel, ContentType, Lenguage, Metadata, Content, Group
from .service.channel_service import channel_service
from .service.content_service import content_sevrice
from .serializers import (
    ChannelSerializer,
    ContentTypeSerializer,
    LenguageSerializer,
    MetadataSerializer,
    ContentSerializer,
    GroupSerializer,
)


class GroupAll(generics.ListCreateAPIView):
    serializer_class = GroupSerializer

    def get_queryset(self) -> QuerySet:
        queryset = Group.objects.all()
        name = self.request.query_params.get("name", None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class GroupCrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ChannelCrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

    def delete(self, request, *args, **kwargs):
        content = self.get_object()
        channel_service.delete_parent_channel_if_no_subchannels(content)

        return super().delete(request, *args, **kwargs)


class ChannelAll(generics.ListCreateAPIView):
    serializer_class = ChannelSerializer

    def get_queryset(self) -> QuerySet:
        queryset = Channel.objects.all()
        groups = self.request.query_params.get("groups", None)
        if groups is not None:
            queryset = queryset.filter(groups__in=[groups])

        return queryset


class ContentTypeCrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContentType.objects.all()
    serializer_class = ContentTypeSerializer


class ContentTypeAll(generics.ListCreateAPIView):
    serializer_class = ContentTypeSerializer

    def get_queryset(self) -> QuerySet:
        queryset = ContentType.objects.all()
        name = self.request.query_params.get("name", None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class LenguageCrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lenguage.objects.all()
    serializer_class = LenguageSerializer


class LenguageAll(generics.ListCreateAPIView):
    serializer_class = LenguageSerializer

    def get_queryset(self) -> QuerySet:
        queryset = Lenguage.objects.all()
        name = self.request.query_params.get("name", None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class MetadataCrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = Metadata.objects.all()
    serializer_class = MetadataSerializer


class MetadataAll(generics.ListCreateAPIView):
    serializer_class = MetadataSerializer

    def get_queryset(self) -> QuerySet:
        queryset = Metadata.objects.all()
        id_filter = self.request.query_params.get("id", None)
        if id_filter is not None:
            queryset = queryset.filter(id__icontains=id_filter)
        return queryset


class ContentCrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    def delete(self, request, *args, **kwargs):
        content = self.get_object()
        content_sevrice.delete_channel_if_no_contents(content)

        return super().delete(request, *args, **kwargs)


class ContentAll(generics.ListCreateAPIView):
    serializer_class = ContentSerializer

    def get_queryset(self) -> QuerySet:
        queryset = Content.objects.all()
        id_filter = self.request.query_params.get("id", None)
        if id_filter is not None:
            queryset = queryset.filter(id__icontains=id_filter)
        content_type_id_filter = self.request.query_params.get(
            "content_type", None
        )
        if content_type_id_filter is not None:
            queryset = queryset.filter(
                contennt_type_id__icontains=content_type_id_filter
            )

        return queryset


class GetChannelRating(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs["pk"]
        response = channel_service.get_rating(id)

        return Response(response)


class ExportRaitings(APIView):
    def get(self, request, *args, **kwargs):
        response = channel_service.export_rattings_csv()
        return response
