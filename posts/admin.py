from django.contrib import admin
from .models import PostModel,BuildModel

admin.site.register(PostModel)
admin.site.register(BuildModel)