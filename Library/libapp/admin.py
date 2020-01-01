from django.contrib import admin
from libapp.models import LibraryModel

# Register your models here.
class LibraryAdmin(admin.ModelAdmin):
    list_display=['rankno','bname','author','type']

admin.site.register(LibraryModel,LibraryAdmin)
