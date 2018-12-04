from django.contrib import admin
from .models import Passing, Rushing, Receiving, Kicking, Punting, Defense, GiveTake, Returning
# Register your models here.

admin.site.register(Passing)
admin.site.register(Rushing)
admin.site.register(Receiving)
admin.site.register(Kicking)
admin.site.register(Punting)
admin.site.register(Defense)
admin.site.register(GiveTake)
admin.site.register(Returning)
