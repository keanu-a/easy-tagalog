from django.contrib import admin
from .models import Word, English, Translation, Aspect, LinkedWord

admin.site.register(Word)
admin.site.register(English)
admin.site.register(Translation)
admin.site.register(Aspect)
admin.site.register(LinkedWord)