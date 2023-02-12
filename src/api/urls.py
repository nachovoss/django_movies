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
    path(
        "channel/export_ratings/",
        ExportRaitings.as_view(),
        name="export_ratings",
    ),
    path(
        "channel/get_rating/<int:pk>",
        GetChannelRating.as_view(),
        name="get_rating",
    ),
    path("channel/<int:pk>", ChannelCrud.as_view(), name="channel_crud"),
    path("channel/", ChannelAll.as_view(), name="channel"),
    path(
        "content_type/<int:pk>",
        ContentTypeCrud.as_view(),
        name="content_type_crud",
    ),
    path("content_type/", ContentTypeAll.as_view(), name="content_type"),
    path("lenguage/<int:pk>", LenguageCrud.as_view(), name="lenguage_crud"),
    path("lenguage/", LenguageAll.as_view(), name="lenguage"),
    path("metadata/<int:pk>", MetadataCrud.as_view(), name="metadata_crud"),
    path("metadata/", MetadataAll.as_view(), name="metadata"),
    path("content/<int:pk>", ContentCrud.as_view(), name="content_crud"),
    path("content/", ContentAll.as_view(), name="content"),
]
