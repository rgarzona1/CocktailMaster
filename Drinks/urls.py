from django.contrib import admin
from django.urls import path
from Drinks.views import home, obtener_cocteles

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  home),
    path('api/cocktails/', obtener_cocteles, name='obtener_cocktails')
]
