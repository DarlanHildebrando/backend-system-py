from django.contrib import admin
from .models import Event, Category, Hashtag, EventTicket, EventAndCategory, EventAndHashtag

admin.site.register(Event)
admin.site.register(Category)
admin.site.register(Hashtag)
admin.site.register(EventTicket)
admin.site.register(EventAndCategory)   
admin.site.register(EventAndHashtag)