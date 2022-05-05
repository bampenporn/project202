from django.contrib import admin
from myapp.models import Image, Board, Pin

class ImageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Image, ImageAdmin)

class BoardAdmin(admin.ModelAdmin):
    pass
admin.site.register(Board, BoardAdmin)

class PinAdmin(admin.ModelAdmin):
    pass
admin.site.register(Pin, PinAdmin)