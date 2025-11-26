# urls.py
from django.urls import path

from Perfil import api_views
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.perfil_dashboard, name='perfil_dashboard'),
    path('api/mis-creaciones/', api_views.MisCreacionesList.as_view(), name='api_mis_creaciones'),
    path('api/recetas-guardadas/', api_views.RecetasGuardadasList.as_view(), name='api_recetas_guardadas'),
    path('api/recetas-creadas/', api_views.RecetaListCreateAPIView.as_view(), name='api_recetas_creadas'),
    path('crear-receta/', views.crear_receta, name='crear_receta'),
]
