from django.contrib import admin
from .models import wadu
# Register your models here.
@admin.register(wadu)
class waduAdmin(admin.ModelAdmin):
    list_display =['Title','Titleinarabic','image','descriptioninarabic','description']


#name alquran
# password = alquran786