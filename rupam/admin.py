from django.contrib import admin
from .models import Slider,Blog,Contact,FilesAdmin,Video

# Register your models here.
admin.site.register(Slider)
admin.site.register(Contact)
admin.site.register(FilesAdmin)
admin.site.register(Video)


@admin.register(Blog)

class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)