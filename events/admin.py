from django.contrib import admin
from .models import Event, Category, Hashtag

admin.site.register(Event)
admin.site.register(Category)
admin.site.register(Hashtag)