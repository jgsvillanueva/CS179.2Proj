from django.contrib import admin

# Register your models here.
from .models import Post

# Create your views here.
admin.site.register(Post)
