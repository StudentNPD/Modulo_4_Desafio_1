from ingredientes import vegetales_posibles, proteicos_posibles, masas_posibles

class Pizza:
    # Atributos de clase
    precio = 10000
    tamaño = "Familiar"
    
    @staticmethod
    def validar_ingrediente(ingrediente, opciones):
        return ingrediente in opciones

    def pedido_pizza(self):
        print("Escoje tus ingredientes para la pizza:")

        # Se pide vegetal
        for i in range(2):
            while True:
                vegetal = input(f"Elige el vegetal {i+1} ({', '.join(self.vegetales_disponibles)}): ").lower()
                if self.validar_ingrediente(vegetal, self.vegetales_disponibles):
                    self.ingredientes_vegetales.append(vegetal)
                    break
                print("Ingrediente no válido. Solo esta permitido: tomate, aceitunas, champiñones.")

        # Se pide ingrediente proteico
        proteico = input(f"Elige el ingrediente protéico ({', '.join(self.proteicos_disponibles)}): ").lower()

        # Seleccion de masa
        masa = input(f"Elige el tipo de masa ({', '.join(self.tipos_masa)}): ").lower()
