from django.test import TestCase, Client
from django.urls import reverse
from api.models import Channel, ContentType, Lenguage, Metadata, Content


class TestRating(TestCase):
    def setUp(self):
        self.client = Client()
        self.export_ratings_url = reverse("export_ratings")
        self.get_rating_url = reverse("get_rating", args=[1])
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


class TestChannelViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.channel_url = reverse("channel")
        self.channel_crud_url = reverse("channel_crud", args=[1])
        channel = Channel.objects.create(
            title="Test Channel",
            is_parent=False,
            picture_url="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png",
        )
        channel.save()

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

        response = self.client.get(self.channel_crud_url, args=[1])

        self.assertEquals(response.status_code, 200)

    def test_channel_update(self):
        response = self.client.put(
            self.channel_crud_url,
            {
                "title": "Test Channel",
                "is_parent": True,
                "picture_url": "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png",
            },
            content_type="application/json",
        )
        self.assertEquals(response.status_code, 200)

    def test_parent_channel_update(self):
        response = self.client.put(
            self.channel_crud_url,
            {
                "title": "Test Channel",
                "is_parent": False,
                "picture_url": "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png",
                "parent_channel": 1,
            },
            content_type="application/json",
        )
        # print(response.content)
        self.assertEquals(response.status_code, 400)

    def test_channel_delete(self):
        response = self.client.delete(self.channel_crud_url, format="json")
        self.assertEquals(response.status_code, 204)


class TestContentTypeViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.content_type_url = reverse("content_type")
        self.content_type_crud_url = reverse("content_type_crud", args=[1])
        content_type = ContentType.objects.create(name="Test Content Type")
        content_type.save()

    def test_content_type_all(self):

        response = self.client.get(self.content_type_url)
        self.assertEquals(response.status_code, 200)

    def test_content_type_add(self):
        response = self.client.post(
            self.content_type_url,
            {"name": "Test Content Type 2"},
            format="json",
        )

        self.assertEquals(response.status_code, 201)

    def test_content_type_crud(self):

        response = self.client.get(reverse("content_type_crud", args=[1]))

        self.assertEquals(response.status_code, 200)

    def test_content_type_update(self):
        response = self.client.put(
            self.content_type_crud_url,
            {"name": "Test Content Type Updated"},
            content_type="application/json",
        )

        self.assertEquals(response.status_code, 200)

    def test_content_type_delete(self):
        response = self.client.delete(
            self.content_type_crud_url, format="json"
        )

        self.assertEquals(response.status_code, 204)


class TestLenguageViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.lenguage_url = reverse("lenguage")
        self.lenguage_crud_url = reverse("lenguage_crud", args=[1])
        lenguage = Lenguage.objects.create(name="Test Lenguage", alias="tl")
        lenguage.save()

    def test_lenguage_all(self):

        response = self.client.get(self.lenguage_url)
        self.assertEquals(response.status_code, 200)

    def test_lenguage_add(self):
        response = self.client.post(
            self.lenguage_url,
            {"name": "Test Lenguage 2", "alias": "tl2"},
            format="json",
        )

        self.assertEquals(response.status_code, 201)

    def test_lenguage_crud(self):
        response = self.client.get(reverse("lenguage_crud", args=[1]))

        self.assertEquals(response.status_code, 200)

    def test_lenguage_update(self):
        response = self.client.put(
            self.lenguage_crud_url,
            {"name": "Test Lenguage Updated", "alias": "tlu"},
            content_type="application/json",
        )
        self.assertEquals(response.status_code, 200)

    def test_lenguage_delete(self):
        response = self.client.delete(self.lenguage_crud_url, format="json")

        self.assertEquals(response.status_code, 204)


class TestMetadataViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.metadata_url = reverse("metadata")
        self.metadata_crud_url = reverse("metadata_crud", args=[1])
        channel = Channel.objects.create(
            title="Test Channel",
            is_parent=False,
            picture_url="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png",
        )
        channel.save()
        lenguage = Lenguage.objects.create(name="Test Lenguage", alias="tl")
        lenguage.save()
        content_type = ContentType.objects.create(name="Test Content Type")
        content_type.save()
        content = Content.objects.create(
            title="Rites of Passage S1 E1",
            file_url="https://www.youtube.com/watch?v=_LHYMTyp74s&ab_channel=SeriesJL",
            rating=9,
            content_type=content_type,
            parent_channel=channel,
        )
        content.save()
        metadata = Metadata.objects.create(
            extra_data="Test Metadata",
            description="Test Description",
            authors="Test Author",
            genere="Test Genere",
            lenguage_id=lenguage,
            content_id=content,
        )
        metadata.save()

    def test_metadata_all(self):

        response = self.client.get(self.metadata_url)
        self.assertEquals(response.status_code, 200)

    def test_metadata_add(self):
        response = self.client.post(
            self.metadata_url,
            {
                "extra_data": "Test Metadata 2",
                "description": "Test Description 2",
                "authors": "Test Author 2",
                "genere": "Test Genere 2",
                "lenguage_id": 1,
                "content_id": 1,
            },
            format="json",
        )

        self.assertEquals(response.status_code, 201)

    def test_metadata_crud(self):
        response = self.client.get(reverse("metadata_crud", args=[1]))

        self.assertEquals(response.status_code, 200)

    def test_metadata_update(self):
        response = self.client.put(
            self.metadata_crud_url,
            {
                "extra_data": "Test Metadata Updated",
                "description": "Test Description Updated",
                "authors": "Test Author Updated",
                "genere": "Test Genere Updated",
                "lenguage_id": 1,
                "content_id": 1,
            },
            content_type="application/json",
        )
        self.assertEquals(response.status_code, 200)

    def test_metadata_delete(self):
        response = self.client.delete(self.metadata_crud_url, format="json")

        self.assertEquals(response.status_code, 204)


class TestContentViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.content_url = reverse("content")
        self.content_crud_url = reverse("content_crud", args=[1])
        channel = Channel.objects.create(
            title="Test Channel",
            is_parent=False,
            picture_url="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png",
        )
        channel.save()
        content_type = ContentType.objects.create(name="Test Content Type")
        content_type.save()
        content = Content.objects.create(
            title="Rites of Passage S1 E1",
            file_url="https://www.youtube.com/watch?v=_LHYMTyp74s&ab_channel=SeriesJL",
            rating=9,
            content_type=content_type,
            parent_channel=channel,
        )
        content.save()

    def test_content_all(self):

        response = self.client.get(self.content_url)
        self.assertEquals(response.status_code, 200)

    def test_content_add(self):
        response = self.client.post(
            self.content_url,
            {
                "title": "Test Content 2",
                "file_url": "https://www.youtube.com/watch?v=_LHYMTyp74s&ab_channel=SeriesJL",
                "rating": 9,
                "content_type": 1,
                "parent_channel": 1,
            },
            format="json",
        )

        self.assertEquals(response.status_code, 201)

    def test_content_crud(self):
        response = self.client.get(reverse("content_crud", args=[1]))

        self.assertEquals(response.status_code, 200)

    def test_content_update(self):
        response = self.client.put(
            self.content_crud_url,
            {
                "title": "Test Content Updated",
                "file_url": "https://www.youtube.com/watch?v=_LHYMTyp74s&ab_channel=SeriesJL",
                "rating": 9,
                "content_type": 1,
                "parent_channel": 1,
            },
            content_type="application/json",
        )
        self.assertEquals(response.status_code, 200)

    def test_content_delete(self):
        response = self.client.delete(self.content_crud_url, format="json")

        self.assertEquals(response.status_code, 204)
