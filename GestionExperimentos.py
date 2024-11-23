import datetime 
import statistics

#Atributos: Nombre experimentos, Fecha realización (DD/MM/AAAA), Tipo experimento y resultados numericos

experiments = []
categories = ["Quimica", "Biologia", "Fisica"]
results = []

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
#CATEGORIAS-----------------------
    print("Tipos de experimento disponibles:", ", ".join(categories))
    while True:
        tipo = input("Tipo de experimento: ")
        if tipo in categories: #Si el tipo de experimento esta en la lista categorias es valido
            break  
        else:
            print("Tipo no válido. Debe ser uno de los siguientes:", ", ".join(categories))

#RESULTADOS ----------------------|
    results = []
    while True:
        try:
            # Se ingresa cada resultado como un número entero
            resultado = int(input("Ingrese un resultado : (En numeros: !):"))
            results.append(resultado)
            print("\nResultado agregado con éxito.")
            print("Si termino presione solo -ENTER-")
        except ValueError:
            # Permite terminar la entrada de resultados
            if input("¿Terminar entrada de resultados? (Presione: (s) para salir): ").lower() == "s":
                break

    # Guardar los datos del experimento 
    experiments.append({
        "nombre": nameExperiment,
        "fecha": fecha.strftime("%d/%m/%Y"), 
        "tipo": tipo,
        "resultados": results
    })
    print("Experimento agregado con éxito.")

#funcion para visualizar experimentos
def mostrar_Experimentos(): 
    print("\n--- Lista de Experimentos ---")
    if not experiments:
        print("No hay experimentos registrados.")
        return
    for i, exp in enumerate(experiments, 1): #Enumerar los experimentos indica que inicia en 1
        # i es el contador de experimentos y exp es el valor de cada experimento
        print(f"{i}. Nombre: {exp['nombre']}, Fecha: {exp['fecha']}, Tipo: {exp['tipo']}")
        print("   Resultados:", exp['resultados'])

def calcular_Experimentos(): #funcion para calcular Estadisticas promedio maximo y minimo de experimentos
    """
    Permite al usuario calcular estadísticas básicas (promedio, máximo y mínimo) 
    de los resultados de un experimento seleccionado.
    """
    print("\n--- Análisis de Resultados ---")
    mostrar_Experimentos()
    if not experiments:
        return
    try:
        # Solicitar al usuario que seleccione un experimento por número
        indice = int(input("Seleccione el número del experimento a analizar: ")) - 1
        exp = experiments[indice]
        resultados = exp["resultados"]
        if not resultados:
            print("El experimento seleccionado no tiene resultados.")
            return
        # Cálculos de estadísticas
        promedio = sum(resultados) / len(resultados)
        maximo = max(resultados)
        minimo = min(resultados)
        print(f"Estadísticas del experimento '{exp['nombre']}':")
        print(f"  Promedio: {promedio:.2f}, Máximo: {maximo:.2f}, Mínimo: {minimo:.2f}") #2 decimales
    except (IndexError, ValueError):
        print("Selección inválida.")

def comparar_Experimentos(): #funcion para comparar experimentos = 2 o mas 
    pass

def eliminar_Experimentos(): #funcion para eliminar un experimento
    pass

def generar_Informe(): #funcion para generar informe tipo resumen + Estadisticas
    """
    Crea un informe que incluye la descripción de todos los experimentos,
    sus resultados y estadísticas. Guarda el informe en un archivo .txt.
    """
    print("\n--- Generación de Informe ---")
    if not experiments:
        print("No hay experimentos para generar un informe.")
        return
    
    # Solicitar el nombre del archivo para guardar el informe
    nombre_archivo = input("Nombre del archivo para guardar el informe (sin extensión): ") + ".txt"
    with open(nombre_archivo, "w") as archivo:
        archivo.write("Informe de Proyecto de Investigación Científica\n")
        archivo.write("=" * 50 + "\n")
        for exp in experiments:
            archivo.write(f"Nombre: {exp['nombre']}\n")
            archivo.write(f"Fecha: {exp['fecha']}\n")
            archivo.write(f"Tipo: {exp['tipo']}\n")
            archivo.write(f"Resultados: {exp['resultados']}\n")
            # Si hay resultados, incluir estadísticas
            if exp["resultados"]:
                promedio = sum(exp["resultados"]) / len(exp["resultados"])
                archivo.write(f"  Promedio: {promedio:.2f}, Máximo: {max(exp['resultados']):.2f}, Mínimo: {min(exp['resultados']):.2f}\n")
            archivo.write("-" * 50 + "\n")
    print(f"Informe guardado como '{nombre_archivo}'.")


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

    #"""
    #Muestra el menú principal con opciones para gestionar experimentos,
    #analizarlos, generar informes o salir del programa.
    #"""
while True:
    print("|=======>  Menu:  <=======|")
    print("| 1. Agregar Experimento  |")
    print("| 2. Mostrar Experimentos |")
    print("| 3. Calcular Estadisticas|")
    print("| 4. Comparar Experimentos|")
    print("| 5. Eliminar Experimento |")
    print("| 6. Generar Informe      |")
    print("| 7. Salir                |")
    print("|=========================|")
        
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        add_experiments()
    elif opcion == "2":
        mostrar_Experimentos()
    elif opcion == "3":
        calcular_Experimentos()
    elif opcion == "6":
        generar_Informe()
    elif opcion == "7":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")

# Ejecución del programa
if __name__ == "__main__":
    menu()  # Llama al menú principal para iniciar la interacción



