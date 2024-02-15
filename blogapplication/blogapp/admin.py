from django.contrib import admin
from .models import  Bloguser
from .models import  Blog
# Register your models here.


admin.site.register(Blog)


admin.site.register(Bloguser)