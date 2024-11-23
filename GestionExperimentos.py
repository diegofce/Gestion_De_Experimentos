import datetime 
import statistics
from tabulate import tabulate 

#Atributos: Nombre experimentos, Fecha realización (DD/MM/AAAA), Tipo experimento y resultados numericos

class Experiments:
    # función de inicialización
    def __init__(self, nameExperiment, dateExperiment, typeExperiment, resultsExperiment):
        self.nameExperiment = nameExperiment
        self.dateExperiment = dateExperiment
        self.typeExperiment = typeExperiment
        self.resultsExperiment = resultsExperiment
        
#funcion para agregar experimentos
def add_experiments(experiments): #funcion para agregar experimentos
    """
    Permite al usuario agregar un nuevo experimento ingresando su nombre, 
    fecha de realización, tipo y una lista de resultados numéricos.
    """
    print("\n--- Agregar Experimento ---")
    nameExperiment = input("Ingrese el nombre del experimento: ")
    
    while True:                             # Validar la fecha del experimento con el formato: DD/MM/AAAA
        dateExperiment_str = input("Ingrese la fecha de realización (ejm 23/11/2024): ")
        try:
            dateExperiment = datetime.datetime.strptime(dateExperiment_str, "%d/%m/%Y")
            break  
        except ValueError:
            print("Fecha no válida. Por favor, usar el formato DD/MM/AAAA")

    typeExperiments = ['a', 'b', 'c'] # tipos de experimentos disponibles
    while True:                     # Validación del tipo de experimento
        typeExperiment = input('Ingrese la categoría del experimento (Biología, Física o Química): ')
        if typeExperiment in typeExperiments: #Si el tipo de experimento esta en la lista categorias es valido
            break  
        else:
            print("Tipo no válido. Debe ser uno de los siguientes:", ", ".join(typeExperiments))

    resultsExperiment = []    #RESULTADOS ----------------------|
    while True:
        try:
            # Se ingresa cada resultado como un número entero
            result = int(input("Ingrese un resultado : (En numeros: !):"))
            resultsExperiment.append(result)
            print("\nResultado agregado con éxito.")
            print("Si termino presione solo -ENTER-")
        except ValueError:
            # Permite terminar la entrada de resultados
            if input("¿Terminar entrada de resultados? (Presione: (s) para salir): ").lower() == "s":
                break

    # Guardar los datos del experimento 
    experiment = Experiments(nameExperiment, dateExperiment, typeExperiment, resultsExperiment)
    experiments.append(experiment)
    print("Experimento agregado con éxito.")

#funcion para visualizar experimentos
def visualize_experiments(experiments): 
    print("\n--- Lista de Experimentos ---")
    if not experiments:
        print("No hay experimentos registrados")
        return
    for i, exp in enumerate(experiments, start=1):    #Enumerar los experimentos indica que inicia en 1
                                                # i es el contador de experimentos y exp es el valor de cada experimento
        print(f"\n{i}. Nombre: {exp.nameExperiment}, Fecha: {exp.dateExperiment.strftime('%d%m%Y')}, Tipo: {exp.typeExperiment}, Resultados: {exp.resultsExperiment}")

#funcion para calcular Estadisticas promedio maximo y minimo de experimentos
def calculate_experiments(experiments): 
    """
    Permite al usuario calcular estadísticas básicas (promedio, máximo y mínimo) 
    de los resultados de un experimento seleccionado.
    """
    print("\n--- Análisis de Resultados ---")
    visualize_experiments(experiments)
    if not experiments:
        return
    try:
        # Solicitar al usuario que seleccione un experimento por número
        index = int(input("Seleccione el número del experimento a analizar: ")) - 1
        exp = experiments[index]
        results = exp.resultsExperiment
        if not results:
            print("El experimento seleccionado no tiene resultados.")
            return
        # Cálculos de estadísticas
        average = sum(results) / len(results)
        numMax = max(results)
        numMin = min(results)
        print(f"Estadísticas del experimento '{exp.nameExperiment}':")
        print(f"  Promedio: {average:.2f}, Máximo: {numMax:.2f}, Mínimo: {numMin:.2f}") #2 decimales
    except (IndexError, ValueError):
        print("Selección inválida.")

def compare_experiments(experiments): #funcion para comparar experimentos = 2 o mas 
    pass

def eliminar_Experimentos(): #funcion para eliminar un experimento
    pass

def generate_Report(experiments): #funcion para generar informe tipo resumen + Estadisticas
    """
    Crea un informe que incluye la descripción de todos los experimentos,
    sus resultados y estadísticas. Guarda el informe en un archivo .txt.
    """
    print("\n--- Generación de Informe ---")
    if not experiments:
        print("No hay experimentos para generar un informe.")
        return
    
    # Solicitar el nombre del archivo para guardar el informe
    nameFile = input("Ingrese el nombre del archivo para guardar el informe (sin extensión): ") + ".txt"
    with open(nameFile, "w") as fileN:
        fileN.write("Informe de Proyecto de Investigación Científica\n")
        fileN.write("=" * 50 + "\n")
        for exp in experiments:
            fileN.write(f"Nombre: {exp.nameExperiment}\n")
            fileN.write(f"Fecha: {exp.dateExperiment.strftime('%d%m%Y')}\n")
            fileN.write(f"Tipo: {exp.typeExperiment}\n")
            fileN.write(f"Resultados: {exp.resultsExperiment}\n")
            # Si hay resultados, incluir estadísticas
            if exp.resultsExperiment:
                average = sum(exp.resultsExperiment) / len(exp.resultsExperiment)
                fileN.write(f"  Promedio: {average:.2f}, Máximo: {max(exp.resultsExperiment):.2f}, Mínimo: {min(exp.resultsExperiment):.2f}\n")
            fileN.write("-" * 50 + "\n")
    print(f"Informe guardado como '{nameFile}'.")

    #"""
    #Muestra el menú principal con opciones para gestionar experimentos,
    #analizarlos, generar informes o salir del programa.
    #"""
def menu():
    experiments = []
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
            add_experiments(experiments)
        elif opcion == "2":
            visualize_experiments(experiments)
        elif opcion == "3":
            calculate_experiments(experiments)
        elif opcion == "4":
            compare_experiments(experiments)
        elif opcion == "6":
            generate_Report(experiments)
        elif opcion == "7":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecución del programa
if __name__ == "__main__":
      # Llama al menú principal para iniciar la interacción
    menu()