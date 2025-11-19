from django.contrib import admin
from .models import User, RecetaCreada, RecetaGuardada

# Register your models here.

admin.site.register(User)
admin.site.register(RecetaCreada)
admin.site.register(RecetaGuardada)