from django.contrib import admin
from .models import Channel, ContentType, Lenguage, Metadata, Content

admin.site.register(Channel)
admin.site.register(ContentType)
admin.site.register(Lenguage)
admin.site.register(Metadata)
admin.site.register(Content)
