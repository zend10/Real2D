from django.contrib import admin
from .models import Series, Location, SeriesLocation


admin.site.register(Series)
admin.site.register(Location)
admin.site.register(SeriesLocation)