from django.db import models
from datetime import datetime

# Create your models here.


class Group(models.Model):
    """Groups model."""

    id: int = models.AutoField(primary_key=True)
    name: str = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Channel(models.Model):
    """Channel model."""

    id: int = models.AutoField(primary_key=True)
    title: str = models.CharField(max_length=255)
    picture_url: str = models.URLField(max_length=255)
    is_parent: bool = models.BooleanField(default=False)
    parent_channel: int = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, blank=True
    )
    date_created: datetime = models.DateTimeField(auto_now_add=True)
    groups: int = models.ManyToManyField(Group, related_name="channels")

    def __str__(self) -> str:
        return self.title


class ContentType(models.Model):
    """Content type model."""

    id: int = models.AutoField(primary_key=True)
    name: str = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Lenguage(models.Model):
    """Lenguage model."""

    id: int = models.AutoField(primary_key=True)
    name: str = models.CharField(max_length=255)
    alias: str = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Metadata(models.Model):
    """Metadata model."""

    id: int = models.AutoField(primary_key=True)
    extra_data: str = models.TextField(
        null=True, blank=True
    )  # JSON field if needed in the future
    lenguage_id: int = models.ForeignKey(Lenguage, on_delete=models.CASCADE)
    authors: str = models.CharField(max_length=255, null=True, blank=True)
    description: str = models.TextField(null=True, blank=True)
    genere: str = models.CharField(max_length=255, null=True, blank=True)
    content_id: int = models.ForeignKey(
        "Content", on_delete=models.CASCADE, null=True
    )

    def __str__(self) -> str:
        return str(self.id)


class Content(models.Model):
    """Content model."""

    id: int = models.AutoField(primary_key=True)
    title: str = models.CharField(max_length=255)
    content_type: int = models.ForeignKey(
        ContentType, on_delete=models.CASCADE
    )
    file_url: str = models.URLField(max_length=255)
    date_created: datetime = models.DateTimeField(auto_now_add=True)
    rating: int = models.IntegerField(default=0)
    parent_channel: int = models.ForeignKey(
        Channel, null=True, blank=True, on_delete=models.SET_NULL
    )
    # date_modified = models.DateTimeField(auto_now=True, null=True, blank=True)
    # date_deleted = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.title
