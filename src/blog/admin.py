from django.contrib import admin
from .models import Post ,Tag, Categorie, PostParagraphs , Comment
# Register your models here.

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Categorie)
admin.site.register(PostParagraphs)
admin.site.register(Comment)