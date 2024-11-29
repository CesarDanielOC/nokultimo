from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Base/', include('app_base.urls')),
    path('Paciente/', include('paciente_app.urls')),  
    path('Proveedor/', include('proveedor_app.urls')),
    path('Promocion/', include('promocion_app.urls')),
    path('Producto/', include('producto_app.urls')),
    path('Pedido/', include('pedido_app.urls')),
    path('', include('app_base.urls')),
]
