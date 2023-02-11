from django.urls import path
from .views import (
    ExportRaitings,
    GetChannelRating,
    ChannelCrud,
    ChannelAll,
    ContentTypeCrud,
    ContentTypeAll,
    LenguageCrud,
    LenguageAll,
    MetadataCrud,
    MetadataAll,
    ContentCrud,
    ContentAll,
)

urlpatterns = [
    # path("channelpost/", post_channel),
    path("channel/export_ratings/", ExportRaitings.as_view()),
    path("channel/get_rating/<int:pk>", GetChannelRating.as_view()),
    path("channel/<int:pk>", ChannelCrud.as_view()),
    path("channel/", ChannelAll.as_view()),
    path("content_type/<int:pk>", ContentTypeCrud.as_view()),
    path("content_type/", ContentTypeAll.as_view()),
    path("lenguage/<int:pk>", LenguageCrud.as_view()),
    path("lenguage/", LenguageAll.as_view()),
    path("metadata/<int:pk>", MetadataCrud.as_view()),
    path("metadata/", MetadataAll.as_view()),
    path("content/<int:pk>", ContentCrud.as_view()),
    path("content/", ContentAll.as_view()),
]
