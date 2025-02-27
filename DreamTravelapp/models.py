from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

#Categorias de los viajes
class Categorias22(models.Model):
        id_categoria2 = models.AutoField(primary_key=True)
        nombreCategoria2= models.CharField(max_length=150)
class Meta:
        db_table = 'categorias22'
        verbose_name = 'Categoria22'
        verbose_name_plural = 'Categorias22'
def __str__(self):
        return self.nombreCategoria2
def __unicode__(self):
        return self.nombreCategoria2
       

       
        

    

#Rol
class Rol(models.Model):
    ADMINISTRADOR = 'Administrador'
    USUARIO = 'Usuario'
    FULL_STACK = 'Full Stack'


    ROLES_CHOICES = [
        (ADMINISTRADOR, 'Administrador'),
        (USUARIO, 'Usuario'),
        (FULL_STACK, 'Full Stack'),
    ]
    id_rol = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=100, choices=ROLES_CHOICES, default=USUARIO)


    class Meta:
        db_table = 'rol'
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'


    def __str__(self):
        return self.nombre_rol
   
#Metodo de pago del usuario
class MetodoPago(models.Model):
    id_metodoPago = models.AutoField(primary_key=True)
    nombrePago = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'metodo_pago'
        verbose_name = 'Metodos De Pago'
        verbose_name_plural = 'Metodos de pagos'
    
    def __str__(self):
        return self.nombrePago
    
    def __unicode__(self):
        return self.nombrePago

   
#Categorias de los viajes
class Categorias(models.Model):
        id_categoria = models.AutoField(primary_key=True)
        nombreCategoria = models.CharField(max_length=150)
class Meta:
        db_table = 'categorias'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
def __str__(self):
        return self.nombreCategoria
def __unicode__(self):
        return self.nombreCategoria
       


#Clase de usuario  
class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=100)
    apellido_usuario = models.CharField(max_length=100)
    passw = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    dni = models.CharField(max_length=8, validators=[MinLengthValidator(7), MaxLengthValidator(8)])
    telefono = models.CharField(max_length=50)
    mail = models.EmailField(unique=True)
    id_metodoPago = models.ForeignKey(MetodoPago, db_column='id_metodoPago', on_delete=models.CASCADE,)
    id_rol = models.ForeignKey(Rol, db_column='nombre_rol', on_delete=models.CASCADE,default=1,)
    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    def __str__(self):
        return f'{self.nombre_usuario} {self.apellido_usuario}'
    def __unicode__(self):
        return f'{self.nombre_usuario} {self.apellido_usuario}'
   
#Destinos de viaje
#Agregamos un validador de precio
def positive_price_validator(value):
    if value < 0:
        raise ValidationError('El precio debe ser un valor positivo.')
#Agregamos un validador de stock de viajes
def positive_viaje_validator(value):
    if value < 0:
        raise ValidationError('El stock del viaje debe ser igual a 0, o un valor positivo.')
    
    
#Clase Nosotros
class Nosotros(models.Model):
    id_nosotros = models.AutoField(primary_key=True)
    nombre_apellido = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    imagen = models.CharField(max_length=100)
    id_rol = models.ForeignKey('Rol', db_column='id_rol', on_delete=models.CASCADE, default=3)

    class Meta:
        db_table = 'nosotros'
        verbose_name = 'Nosotros'
        verbose_name_plural = 'Nosotros'

    def __str__(self):
        return self.nombre_apellido
   
class Destinos(models.Model):
    id_destino = models.AutoField(primary_key=True)
    nombre_Destino = models.CharField(max_length=150)
    descripcion = models.TextField(default='descripcion', blank=False)
    image = models.URLField(max_length=200, blank=True)  # URLField para imágenes externas
    precio_Destino = models.DecimalField(max_digits=12, decimal_places=2, validators=[positive_price_validator])
    fecha_salida = models.DateTimeField(blank=False)
    cantidad_Disponible = models.IntegerField(default=12, validators=[positive_viaje_validator])
    id_metodoPago = models.ForeignKey('MetodoPago', db_column='id_metodoPago', on_delete=models.CASCADE)
    id_categoria = models.ForeignKey('Categorias',db_column='id_categoria', on_delete=models.CASCADE)

    class Meta:
        db_table = 'destinos'
        verbose_name = 'Destino'
        verbose_name_plural = 'Destinos'
    
    def __str__(self):
        return self.nombre_Destino


class Carrito(models.Model):
    id_compra = models.AutoField(primary_key=True)
    cantidad = models.DecimalField(max_digits=3, decimal_places=0, validators=[positive_price_validator])
    id_metodoPago = models.ForeignKey(MetodoPago, db_column='id_metodoPago', on_delete=models.CASCADE)
    id_destino = models.ForeignKey(Destinos, db_column='id_destino', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    class Meta:
        db_table = 'carrito'
        verbose_name = 'Carrito'
        verbose_name_plural = 'Carrito'
    
    def __str__(self):
        return f"{self.user} - {self.id_destino} - {self.cantidad}"

    
    def __unicode__(self):
        return f'{self.user.username} - {self.id_destino.nombre_Destino}'
    
    