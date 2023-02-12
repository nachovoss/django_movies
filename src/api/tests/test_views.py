from django.test import TestCase, Client
from django.urls import reverse
from api.models import Channel, ContentType, Lenguage, Metadata, Content
import json


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.channel_url = reverse("channel")
        self.channel_crud_url = reverse("channel_crud", args=[1])

    def test_channel_all(self):

        response = self.client.get(self.channel_url)
        self.assertEquals(response.status_code, 200)

    def test_channel_add(self):
        response = self.client.post(
            self.channel_url,
            {
                "title": "Test Channel",
                "is_parent": False,
                "picture_url": "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png",
            },
            format="json",
        )

        self.assertEquals(response.status_code, 201)

    def test_channel_crud(self):
        client = Client()
        response = client.get(reverse("channel_crud", args=[1]))
        import ipdb

        ipdb.set_trace()
        self.assertEquals(response.status_code, 200)
