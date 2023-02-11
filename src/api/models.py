from django.db import models

# Create your models here.


class Channel(models.Model):
    """Channel model."""

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    picture_url = models.CharField(max_length=255)
    is_parent = models.BooleanField(default=False)
    parent_channel = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ContentType(models.Model):
    """Content type model."""

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Lenguage(models.Model):
    """Lenguage model."""

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Metadata(models.Model):
    """Metadata model."""

    id = models.AutoField(primary_key=True)
    extra_data = models.TextField(
        null=True, blank=True
    )  # JSON field if needed in the future
    lenguage_id = models.ForeignKey(Lenguage, on_delete=models.CASCADE)
    authors = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    genere = models.CharField(max_length=255, null=True, blank=True)
    content_id = models.ForeignKey(
        "Content", on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return str(self.id)


class Content(models.Model):
    """Content model."""

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    file_url = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    parent_channel = models.ForeignKey(
        Channel, null=True, blank=True, on_delete=models.SET_NULL
    )
    # date_modified = models.DateTimeField(auto_now=True, null=True, blank=True)
    # date_deleted = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.title
