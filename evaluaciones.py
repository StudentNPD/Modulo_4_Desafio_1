from pizza import Pizza
from ingredientes import salsas_posibles
#a
print("Precio:", Pizza.precio)
print("Tamaño:", Pizza.tamano)
#b
print("¿Está 'salsa de tomate' en la lista? :", Pizza.validar_ingrediente("salsa de tomate",salsas_posibles))

#c 
# Crear una instancia de la clase importada, y luego llamar al método del
# requerimiento 3, para que al ejecutar el script se solicite ingredientes y tipo de
# masa al usuario. 
# crear instancia y llamar a la funcion realizar pedido

# instanciar
mi_pizza = Pizza()
# llamar a la función pedido_pizza
mi_pizza.pedido_pizza()

#d
# Usar la función print(), para que al ejecutar el script, luego de que el usuario
# haya ingresado los ingredientes y tipo de masa, se muestre en pantalla los
# ingredientes vegetales, el ingrediente proteico y el tipo de masa de la instancia
# creada en el paso anterior, y si esa instancia es una pizza válida o no.
# imprimir los atributos

print("Ingredientes vegetal:", mi_pizza.ingredientes_vegetales)
print("Tipo de masa:", mi_pizza.tipo_masa)
print("Proteina:", mi_pizza.ingrediente_proteico)
print(mi_pizza.es_valido)

#e
# Usar la función print(), para mostrar en pantalla si la clase Pizza es una pizza
# válida o no, haciendo uso del atributo creado en el requerimiento 4, sin crear
# una instancia de la clase. En este punto, la ejecución del script debe mostrar
# un error (todos los pasos anteriores se deben haber ejecutado correctamente).
print(Pizza.es_valido)
