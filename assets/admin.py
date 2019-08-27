from django.contrib import admin
from assets import models
# Register your models here.
from assets import asset_handler




class AssetAdmin(admin.ModelAdmin):
    list_display = ['Asset', 'System']

admin.site.register(models.Asset)
admin.site.register(models.System)




