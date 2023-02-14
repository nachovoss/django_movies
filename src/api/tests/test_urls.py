from django.test import SimpleTestCase
from django.urls import reverse, resolve
from api.views import (
    ChannelAll,
    ChannelCrud,
    ContentTypeAll,
    ContentTypeCrud,
    LenguageAll,
    LenguageCrud,
    MetadataAll,
    MetadataCrud,
    ContentAll,
    ContentCrud,
    GroupAll,
    GroupCrud,
)


class TestUrls(SimpleTestCase):
    def test_channel_url_is_resolved(self):
        url = reverse("channel")
        self.assertEquals(resolve(url).func.view_class, ChannelAll)

    def test_channel_crud_url_is_resolved(self):
        url = reverse("channel_crud", args=[1])
        self.assertEquals(resolve(url).func.view_class, ChannelCrud)

    def test_content_type_url_is_resolved(self):
        url = reverse("content_type")
        self.assertEquals(resolve(url).func.view_class, ContentTypeAll)

    def test_content_type_crud_url_is_resolved(self):
        url = reverse("content_type_crud", args=[1])
        self.assertEquals(resolve(url).func.view_class, ContentTypeCrud)

    def test_lenguage_url_is_resolved(self):
        url = reverse("lenguage")
        self.assertEquals(resolve(url).func.view_class, LenguageAll)

    def test_lenguage_crud_url_is_resolved(self):
        url = reverse("lenguage_crud", args=[1])
        self.assertEquals(resolve(url).func.view_class, LenguageCrud)

    def test_metadata_url_is_resolved(self):
        url = reverse("metadata")
        self.assertEquals(resolve(url).func.view_class, MetadataAll)

    def test_metadata_crud_url_is_resolved(self):
        url = reverse("metadata_crud", args=[1])
        self.assertEquals(resolve(url).func.view_class, MetadataCrud)

    def test_content_url_is_resolved(self):
        url = reverse("content")
        self.assertEquals(resolve(url).func.view_class, ContentAll)

    def test_content_crud_url_is_resolved(self):
        url = reverse("content_crud", args=[1])
        self.assertEquals(resolve(url).func.view_class, ContentCrud)

    def test_group_url_is_resolved(self):
        url = reverse("group")
        self.assertEquals(resolve(url).func.view_class, GroupAll)

    def test_group_crud_url_is_resolved(self):
        url = reverse("group_crud", args=[1])
        self.assertEquals(resolve(url).func.view_class, GroupCrud)
