import datetime 

#Atributos: Nombre, Fecha (DD/MM/AAAA), Tipo y resultados numericos

Experiments = []

def add_experiments(): #funcion para agregar experimentos
    """
    Permite al usuario agregar un nuevo experimento ingresando su nombre, 
    fecha de realización, tipo y una lista de resultados numéricos.
    """
    print("\n--- Agregar Experimento ---")
    nameExperiment = input("Nombre del experimento: ")

    # Validar la fecha del experimento con el formato: DD/MM/AAAA

    while True: 
        fecha = input("Fecha de realización (DD/MM/AAAA): ")
        try:
            fecha = datetime.datetime.strptime(fecha, "%d/%m/%Y")
            break  
        except ValueError:
            print("Fecha no válida. Por favor, use el formato DD/MM/AAAA.")


    # Validación del tipo de experimento
    categorias = ["Química", "Biología", "Física"]
    print("Tipos de experimento disponibles:", ", ".join(categorias))
    while True:
        tipo = input("Tipo de experimento: ")
        if tipo in categorias:
            break  # El tipo es válido
        print("Tipo no válido. Debe ser uno de los siguientes:", ", ".join(categorias))
    
def mostrar_Experimentos(): #funcion para mostrar experimentos
    pass

def calcular_Experimentos(): #funcion para calcular Estadisticas promedio maximo y minimo de experimentos
    pass    

def comparar_Experimentos(): #funcion para comparar experimentos = 2 o mas 
    pass

def eliminar_Experimentos(): #funcion para eliminar un experimento
    pass

def generar_Informe(): #funcion para generar informe tipo resumen + Estadisticas
    pass

def menu(): #funcion para mostrar menu
    print("|=======>  Menu:  <=======|")
    print("| 1. Agregar Experimento  |")
    print("| 2. Mostrar Experimentos |")
    print("| 3. Calcular Estadisticas|")
    print("| 4. Comparar Experimentos|")
    print("| 5. Eliminar Experimento |")
    print("| 6. Generar Informe      |")
    print("| 7. Salir                |")
    print("|=========================|")
    

def main(): #funcion principal, controla el flujo del sistema
    menu()
    pass

main()



