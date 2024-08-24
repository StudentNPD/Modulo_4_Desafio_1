# Desafio 1 - Pizzeria


## Actividad 
1. En el archivo pizza.py, crear una clase que permita crear objetos de tipo Pizza. Considerar qué atributos de clase debe contener la clase, según la descripción del problema.
2. En el mismo archivo y clase del requerimiento anterior, agregar un método que permita validar un elemento dentro de una lista de casos posibles. Este método se debe poder utilizar sin necesidad de crear un objeto de la clase, y debe recibir 2 argumentos:
    a. El elemento a validar (un texto).
     b. Los valores posibles a considerar para el elemento ingresado (una lista de textos).
En caso de que el elemento ingresado como primer argumento se encuentre entre la lista de valores posibles ingresada como segundo argumento, el método debe retornar True. En caso contrario, debe retornar False.
3. En el mismo archivo y clase del requerimiento anterior, agregar un método que permita realizar un pedido. Para ello, dentro de la definición de este método, debe solicitar al usuario ingresar el ingrediente proteico, luego el primer ingrediente vegetal, luego el segundo ingrediente vegetal, y finalmente el tipo de masa. Cada ingreso debe almacenarse (o añadirse, si corresponde) en un atributo de la instancia.
4. Dentro del mismo método del requerimiento 3, una vez asignados los valores a los atributos de la instancia, debe evaluarse si se trata de un ingreso válido (considerar la información de la descripción), usando el método del requerimiento 2. Si los 3 ingredientes y el tipo de masa son válidos, deberá almacenar en un atributo el valor True. En caso contrario, deberá almacenar el valor False. Este atributo permitirá saber si una instancia específica es o no una Pizza válida.
5.En un archivo llamado evaluaciones.py, importe la clase creada en el requerimiento 1 (conteniendo los requerimientos 2, 3 y 4), y realice lo siguiente:
     a. Usar la función print(), para que al ejecutar el script se muestre en pantalla los valores de los atributos de clase de la clase importada, sin crear una instancia de ella. 
     b. Usar la función print(), para que al ejecutar el script se muestre en pantalla si el elemento “salsa de tomate” se encuentra presente en la lista [“salsa de tomate", "salsa bbq"]. Para ello use el método creado en el requerimiento 2, sin crear una instancia de la clase importada.
     c. Crear una instancia de la clase importada, y luego llamar al método del requerimiento 3, para que al ejecutar el script se solicite ingredientes y tipo de masa al usuario. 
     d. Usar la función print(), para que al ejecutar el script, luego de que el usuario haya ingresado los ingredientes y tipo de masa, se muestre en pantalla los ingredientes vegetales, el ingrediente proteico y el tipo de masa de la instancia creada en el paso anterior, y si esa instancia es una pizza válida o no. 
     e. Usar la función print(), para mostrar en pantalla si la clase Pizza es una pizza válida o no, haciendo uso del atributo creado en el requerimiento 4, sin crear una instancia de la clase. En este punto, la ejecución del script debe mostrar un error (todos los pasos anteriores se deben haber ejecutado correctamente).

------------------------------------------

## Prerequisitos

- Sistema Operativos: Windows 10, 11, Linux, iOS
- Python 3.12

## Ejecución

***Windows***

`python evaluaciones.py`

***Linux & iOS***

`python3 evaluaciones.py`

------------------------------------------
## Colaboradores
- [Francisco Colomer](https://github.com/Cy5k0) 
- [Francisco Monroy](https://github.com/fmonroy75)
- [Natalia Peña](https://github.com/StudentNPD)
