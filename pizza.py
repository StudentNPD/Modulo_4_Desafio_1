from ingredientes import vegetales_posibles, proteicos_posibles, masas_posibles

class Pizza:
    # Atributos de clase
    precio = 10000
    tamaño = "Familiar"
    
    @staticmethod
    def validar_ingrediente(ingrediente, opciones):
        return ingrediente in opciones
