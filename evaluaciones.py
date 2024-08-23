from pizza import Pizza
from ingredientes import salsas_posibles
#a
print("Precio:", Pizza.precio)
print("Tamaño:", Pizza.tamaño)
#b
print("¿Está 'salsa de tomate' en la lista? :", Pizza.validar_ingrediente("salsa de tomate",salsas_posibles))

