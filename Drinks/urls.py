from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from Drinks.views import home, obtener_cocteles, tragos_por_alcohol
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  home, name='home'),
    path('api/cocktails/', obtener_cocteles, name='obtener_cocktails'),
    path('tragos/<str:alcohol>/', tragos_por_alcohol, name='tragos_por_alcohol')
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

