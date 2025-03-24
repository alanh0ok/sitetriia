# sitetriia/urls.py
from django.contrib import admin
from django.urls import path
from core import views  # Alterar para importar views de core, não de sitetriia

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Página inicial
    path('triia_hub/', views.triia_hub, name='triia_hub'),
    path('branding/', views.branding, name='branding'),
    path('trafego/', views.trafego_pago, name='trafego_pago'),
    path('contato/', views.contato, name='contato'),
]
