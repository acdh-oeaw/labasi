from django.contrib import admin
from .models import Region, Archive, Dossier, Scribe, Period, TextType

admin.site.register(Region)
admin.site.register(Archive)
admin.site.register(Dossier)
admin.site.register(Scribe)
admin.site.register(Period)
admin.site.register(TextType)
