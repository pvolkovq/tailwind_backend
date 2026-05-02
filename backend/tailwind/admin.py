from django.contrib import admin
from tailwind.models import Portfolio, Subscriber, Artwork, Comment, Like

admin.site.register([Portfolio, Subscriber, Artwork, Comment, Like])

