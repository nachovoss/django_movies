from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Channel, ContentType, Lenguage, Metadata, Content
from .service.channel_service import channel_service
from .serializers import (
    ChannelSerializer,
    ContentTypeSerializer,
    LenguageSerializer,
    MetadataSerializer,
    ContentSerializer,
)


class ChannelCrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class ChannelAll(generics.ListCreateAPIView):
    serializer_class = ChannelSerializer

    def get_queryset(self):
        queryset = Channel.objects.all()
        title = self.request.query_params.get("title", None)
        if title is not None:
            queryset = queryset.filter(title__icontains=title)
        return queryset


class ContentTypeCrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContentType.objects.all()
    serializer_class = ContentTypeSerializer


class ContentTypeAll(generics.ListCreateAPIView):
    serializer_class = ContentTypeSerializer

    def get_queryset(self):
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

    def get_queryset(self):
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

    def get_queryset(self):
        queryset = Metadata.objects.all()
        id_filter = self.request.query_params.get("id", None)
        if id_filter is not None:
            queryset = queryset.filter(id__icontains=id_filter)
        return queryset


class ContentCrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


class ContentAll(generics.ListCreateAPIView):
    serializer_class = ContentSerializer

    def get_queryset(self):
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
