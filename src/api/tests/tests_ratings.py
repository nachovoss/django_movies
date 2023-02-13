from django.test import TestCase, Client
from django.urls import reverse
from api.models import Channel, ContentType, Content


class TestRating(TestCase):
    def setUp(self):
        self.client = Client()
        self.export_ratings_url = reverse("export_ratings")
        self.get_rating_url = reverse("get_rating", args=[1])
        self.content_url = reverse("content")
        content_type = ContentType.objects.create(name="Test Content Type")
        channel = Channel.objects.create(
            title="Test Channel",
            is_parent=True,
            picture_url="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png",
        )
        channel.save()
        subchannel1 = Channel.objects.create(
            title="Test Subchannel 1",
            is_parent=False,
            picture_url="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png",
            parent_channel=channel,
        )
        subchannel1.save()
        subchannel2 = Channel.objects.create(
            title="Test Subchannel 2",
            is_parent=False,
            picture_url="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png",
            parent_channel=channel,
        )
        content1 = Content.objects.create(
            title="Test Content 1",
            parent_channel=subchannel1,
            content_type=content_type,
            file_url="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png",
            rating=9,
        )
        content1.save()
        content2 = Content.objects.create(
            title="Test Content 2",
            parent_channel=subchannel2,
            content_type=content_type,
            file_url="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png",
            rating=8,
        )
        content2.save()
        content3 = Content.objects.create(
            title="Test Content 3",
            parent_channel=subchannel2,
            content_type=content_type,
            file_url="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png",
            rating=7,
        )
        content3.save()

    def test_get_parent_channel_rating(self):
        response = self.client.get(self.get_rating_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data.get("rating"), 8.2)

    def test_get_subchannel_rating(self):
        response = self.client.get(reverse("get_rating", args=[3]))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data.get("rating"), 7.5)

    def test_export_ratings(self):
        response = self.client.get(self.export_ratings_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(
            float(str(response.content).split(",")[3].split("\\")[0]), 8.2
        )
        self.assertEquals(
            float(str(response.content).split(",")[2].split("\\")[0]), 9
        )
        self.assertEquals(
            float(str(response.content).split(",")[4].split("\\")[0]), 7.5
        )
        self.assertEquals(
            response["Content-Disposition"], "attachment; filename=ratings.csv"
        )

    def test_max_min_raiting(self):
        for i in (-1, 11):
            response = self.client.post(
                self.content_url,
                {
                    "title": "Test Content 2",
                    "file_url": "https://www.youtube.com/watch?v=_LHYMTyp74s&ab_channel=SeriesJL",
                    "rating": i,
                    "content_type": 1,
                    "parent_channel": 1,
                },
                format="json",
            )

            self.assertEqual(response.data.get("rating")[0].code, "invalid")
            self.assertEquals(response.status_code, 400)
