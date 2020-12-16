from django.contrib import admin

from .models import Product,Advisor,Blog,BlogComment,Contact,FilesAdmin,KidneycareVideo,Disease,Testimonial,Event,Slider


admin.site.register(Product)
admin.site.register(Advisor)
admin.site.register((BlogComment))
admin.site.register(Contact)
admin.site.register(FilesAdmin)
admin.site.register(KidneycareVideo)
admin.site.register(Blog)
admin.site.register(Testimonial)
admin.site.register(Event)
admin.site.register(Slider)


@admin.register(Disease)

class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)