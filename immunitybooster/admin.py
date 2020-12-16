from django.contrib import admin

from .models import Advisor,Blog,Contact,FilesAdmin,Video,Disease,Testimonial,Event,Slider


admin.site.register(Advisor)
admin.site.register(Contact)
admin.site.register(FilesAdmin)
admin.site.register(Video)
admin.site.register(Testimonial)
admin.site.register(Event)
admin.site.register(Slider)


@admin.register(Disease)

class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)

@admin.register(Blog)

class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)