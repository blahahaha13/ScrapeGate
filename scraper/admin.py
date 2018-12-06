from django.contrib import admin
from .models import Passing, Rushing, Kicking, Punting, Turnovers, Returning, Defense, Receiving

# Register your models here.

admin.site.register(Passing)
admin.site.register(Rushing)
admin.site.register(Receiving)
admin.site.register(Kicking)
admin.site.register(Punting)
admin.site.register(Defense)
admin.site.register(Turnovers)
admin.site.register(Returning)

