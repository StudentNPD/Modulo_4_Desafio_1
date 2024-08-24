from ingredientes import vegetales_posibles, proteicos_posibles, masas_posibles

class Pizza:
    # Atributos de clase
    precio = 10000
    tamano = "familiar"
    vegetales_disponibles = vegetales_posibles
    proteicos_disponibles = proteicos_posibles
    tipos_masa = masas_posibles
    #es_valida = False

    def __init__(self):
        self.ingredientes_vegetales = []
        self.ingrediente_proteico = ""
        self.tipo_masa = ""
        self.es_valida = False

    @classmethod
    def validar_ingrediente(cls, ingrediente, opciones):
        return ingrediente in opciones

    def pedido_pizza(self):
        print("Por favor, elige tus ingredientes:")
        
        # Pedir ingredientes vegetales
        for i in range(2):
            while True:
                vegetal = input(f"Elige el vegetal {i+1} ({', '.join(self.vegetales_disponibles)}): ").lower()
                if Pizza.validar_ingrediente(vegetal, self.vegetales_disponibles):
                    self.ingredientes_vegetales.append(vegetal)
                    break
                print("Ingrediente no válido. Intenta de nuevo.")

        # Pedir ingrediente proteico
        while True:
            proteico = input(f"Elige el ingrediente proteico ({', '.join(self.proteicos_disponibles)}): ").lower()
            if Pizza.validar_ingrediente(proteico, self.proteicos_disponibles):
                self.ingrediente_proteico = proteico
                break
            print("Ingrediente no válido. Intenta de nuevo.")

        # Pedir tipo masa
        while True:
            masa = input(f"Elige el tipo de masa ({', '.join(self.tipos_masa)}): ").lower()
            if Pizza.validar_ingrediente(masa, self.tipos_masa):
                self.tipo_masa = masa
                break
            print("Tipo de masa no válido. Intenta de nuevo.")

        # Validar la pizza
        self.es_valida = len(self.ingredientes_vegetales) == 2 and self.validar_ingrediente(proteico,proteicos_posibles) and self.validar_ingrediente(masa,masas_posibles)
