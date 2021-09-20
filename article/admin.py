from django.contrib import admin
from django.contrib.admin.decorators import register
from article.models import *

admin.site.register(Author)
admin.site.register(Publication)
admin.site.register(Comment)
admin.site.register(Readers)





