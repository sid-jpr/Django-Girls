from django.contrib import admin
# we import (include) the Post model defined in models.py
from .models import Post

# To make our model visible on the admin page, we need to register the model with:
admin.site.register(Post)
