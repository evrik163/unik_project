from django.contrib import admin

from machine_learning.models import FinalRes
from .models import Post


admin.site.register(Post)
admin.site.register(FinalRes)
