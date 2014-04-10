from django.contrib import admin
from winebooking.logic.models import *

class ReservationSlotAdmin(admin.ModelAdmin):
    list_display = ('request', 'start', 'end')

# Register your models here.
admin.site.register(Country)
admin.site.register(Region)
admin.site.register(Profile)
admin.site.register(WineType)
admin.site.register(WineVariety)
admin.site.register(WineAgingType)
admin.site.register(WineColor)
admin.site.register(WineCharacter)
admin.site.register(WineAroma)
admin.site.register(WineTaste)
admin.site.register(Wine)
admin.site.register(WineBottle)
admin.site.register(WineMaker)
admin.site.register(ReservationSlotRequest)
admin.site.register(ReservationSlot, ReservationSlotAdmin)
admin.site.register(ReservationFill)
