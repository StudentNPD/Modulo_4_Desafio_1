from ingredientes import vegetales_posibles, proteicos_posibles, masas_posibles

class Pizza:
    # Atributos de clase
    precio = 10000
    tamaño = "Familiar"
    es_valido = False

    def __init__(self):
        self.ingredientes_vegetales = []
        self.ingrediente_proteico = ""
        self.tipo_masa = ""
    
    @staticmethod
    def validar_ingrediente(ingrediente, opciones):
        return ingrediente in opciones

    def pedido_pizza(self):
        print("Escoje tus ingredientes para la pizza:")

        # Se pide vegetal
        for i in range(2):
            while True:
                vegetal = input(f"Elige el vegetal {i+1} ({', '.join(self.vegetales_posibles)}): ").lower()
                if self.validar_ingrediente(vegetal, self.vegetales_posibles):
                    self.ingredientes_vegetales.append(vegetal)
                    break
                print("Ingrediente no válido. Solo esta permitido: tomate, aceitunas, champiñones.")

        # Se pide ingrediente proteico
       while True:
            proteico = input(f"Elige el ingrediente proteico ({', '.join(self.proteicos_posibles)}): ").lower()
            if self.validar_ingrediente(proteico, self.proteicos_posibles):
                self.ingrediente_proteico = proteico
                break
            print("Ingrediente no válido. Pollo, carne, carne vegetal")

        # Seleccion de masa
       while True:
            masa = input(f"Elige el tipo de masa ({', '.join(self.masas_posibles)}): ").lower()
            if self.validar_ingrediente(masa, self.masas_posibles):
                self.tipo_masa = masa
                break
            print("Tipo de masa no válido. Intenta de nuevo.")


        #valida si esta ok la pizza (True)
        self.es_valido = len(self.ingredientes_vegetales) == 2 and self.ingrediente_proteico and self.tipo_masa
