from django.contrib import admin


#Importo los modelos
from .models import Usuarios
from .models import Destinos
from .models import Categorias
from .models import MetodoPago
from .models import Nosotros
from .models import Carrito
from .models import Rol


#Registro los modelos
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ( 'id_usuario','nombre_usuario', 'apellido_usuario', 'direccion', 'dni', 'telefono', 'mail', 'id_rol')
   
class DestinosAdmin(admin.ModelAdmin):
    list_display = ('id_destino', 'nombre_Destino', 'descripcion', 'image', 'precio_Destino', 'fecha_salida', 'cantidad_Disponible')
    search_fields = ('nombre_Destino', 'descripcion')
    list_filter = ('fecha_salida', 'cantidad_Disponible', 'id_categoria')
    ordering = ('fecha_salida',)
    fields = ('nombre_Destino', 'descripcion', 'image', 'precio_Destino', 'fecha_salida','cantidad_Disponible', 'id_metodoPago', 'id_categoria') 

class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('id_categoria','nombreCategoria',)



class RolAdmin(admin.ModelAdmin):
    list_display = ('nombre_rol',) 

class MetodoPagoAdmin(admin.ModelAdmin):
    list_display = ('id_metodoPago','nombrePago',)


class NosotrosAdmin(admin.ModelAdmin):
    list_display = ('id_nosotros', 'nombre_apellido', 'github', 'linkedin', 'imagen', 'id_rol')
    search_fields = ('nombre_apellido', 'github', 'linkedin')




class CarritoAdmin(admin.ModelAdmin):
    list_display = ('id_compra','cantidad','id_metodoPago', 'id_destino',)


class RolAdmin(admin.ModelAdmin):
    list_display = ('id_rol','nombre_rol',)
   


admin.site.register(Usuarios, UsuariosAdmin)
admin.site.register(Destinos, DestinosAdmin)
admin.site.register(Categorias, CategoriasAdmin)
admin.site.register(MetodoPago, MetodoPagoAdmin)
admin.site.register(Nosotros, NosotrosAdmin)
admin.site.register(Carrito,CarritoAdmin)
admin.site.register(Rol, RolAdmin)
