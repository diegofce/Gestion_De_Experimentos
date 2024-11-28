import datetime 
from tabulate import tabulate  


#se crea la clase experimentos
#Atributos: Nombre experimentos, Fecha realización (DD/MM/AAAA), Tipo experimento y resultados numericos

class Experiments:
    # función de inicialización, recibe los atributos
    def __init__(self, nameExperiment, dateExperiment, typeExperiment, resultsExperiment):
        self.nameExperiment = nameExperiment
        self.dateExperiment = dateExperiment
        self.typeExperiment = typeExperiment
        self.resultsExperiment = resultsExperiment 
      
#funcion para agregar experimentos
def add_experiments(experiments):
    """
    Permite al usuario agregar un nuevo experimento ingresando su nombre, 
    fecha de realización, tipo y una lista de resultados numéricos.
    """
    
    print("\n--- Agregar Experimento ---")
    nameExperiment = input("Ingrese el nombre del experimento: ")
    
    while True:                             
        # Validar la fecha del experimento con el formato: DD/MM/AAAA
        dateExperiment_str = input("Ingrese la fecha de realización (ejm 23/11/2024): ")
        try:
            dateExperiment = datetime.datetime.strptime(dateExperiment_str, "%d/%m/%Y")
            break  
        except ValueError:
            print("Fecha no válida. Por favor, usar el formato DD/MM/AAAA")

    while True: # Validación del tipo de experimento
        try:
            print('Experimentos disponibles:\n1. Biología \n2. Física \n3. Química')
            typeE = int(input('Seleccione la categoría que desee: '))
            if(typeE == 1):
                typeExperiment = 'Biología'
                break
            elif(typeE == 2):
                typeExperiment = 'Física'
                break
            elif(typeE == 3):
                typeExperiment = 'Química'
                break
        except(ValueError):
            print('Tipo no válido. Intente de Nuevo.')

    # Capturar los resultados
    resultsExperiment = []
    cont = 0
    while True:
        try:
            # Se ingresa cada resultado como un número entero
            result = float(input("Ingrese los resultados numéricos de su experimento: (ej: 4.5): "))
            if(result>=0):
                resultsExperiment.append(result)
                cont=cont+1 #cuenta los resultados
                print(f'---resultado #{cont} agregado con éxito---')
            else:
                print('** No se puede ingresar números negativos **')
            if(cont<3):
                print('Por favor ingrese mínimo 3 resultados')
            else:
                print('*** Si termino *** ==>No agregue mas Numeros<== Y Press enter')
        except ValueError:
            # Permite terminar la entrada de resultados
            if cont >= 3 and input("¿Terminar entrada de resultados? (Presione: (s) para salir): ").lower() == "s":
                break
            else:
                print('Debe ingresar al menos 3 resultados antes de finalizar.')

    if not resultsExperiment:  # Validar si la lista de resultados está vacía
        print("No se ingresaron resultados. El experimento no se guardará.")
        return
    # Guardar los datos del experimento 
    experiment = Experiments(nameExperiment, dateExperiment, typeExperiment, resultsExperiment)
    experiments.append(experiment)

    print("--- Experimento agregado con éxito.---")

#funcion para visualizar experimentos
def visualize_experiments(experiments): 
    print("\n--- Lista de Experimentos ---")
    if not experiments:
        print("No hay experimentos registrados")
        return

    table = [
        [i+1, exp.nameExperiment, exp.dateExperiment.strftime('%d/%m/%Y'), exp.typeExperiment, exp.resultsExperiment]
        for i, exp in enumerate(experiments)
    ]
    print(tabulate(table, headers=["#", "Nombre", "Fecha", "Tipo", "Resultados"]))

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

def compare_experiments(experiments):
    print("\n--- Comparar Experimentos ---")
    visualize_experiments(experiments)
    
    indexE = list(map(int, input('Ingrese los números de los experimentos que desea comparar separados por comas: ').split(',')))
    indexE = [i - 1 for i in indexE]

    resultCompare = []
    
    for index in indexE:
        if (0 <= index < len(experiments)):
            exp = experiments[index]
            results = exp.resultsExperiment
            average = sum(results)/len(results)
            maxi = max(results)
            mini = min(results)
            resultCompare.append((exp.nameExperiment, average, maxi, mini))
            print(resultCompare)
        else:
            print(f'Indice {index} no válido')
    for name, averageE, maxiE, minE in resultCompare:
        print(f'Nombre: {name}, Promedio: {averageE}, Maximo: {maxiE}, Mínimo: {minE}')

def erase_experiments(experiments): #funcion para eliminar un experimento
    visualize_experiments(experiments)
    if not experiments:
        return
    try:
        index = int(input("\nSeleccione el número del experimento a eliminar: ")) - 1
        exp = experiments[index]
        print(f'Esta seguro que desea eliminar el experimento {exp.nameExperiment}?')
        conf = input('Si (s) _ No (n)').lower()
        if(conf=='s' or conf=='si'):
            experiments.remove(exp)
            print('**Experimento eliminado con éxito**')
        else:
            return
    except (IndexError,ValueError):
        print('Experimento no existente')

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
        try:
            print("|=======>  Menu:  <=======|")
            print("| 1. Agregar Experimento  |")
            print("| 2. Mostrar Experimentos |")
            print("| 3. Calcular Estadisticas|")
            print("| 4. Comparar Experimentos|")
            print("| 5. Eliminar Experimento |")
            print("| 6. Generar Informe      |")
            print("| 7. Salir                |")
            print("|=========================|")
                
            option = int(input("Seleccione una opción: "))
            if(option<1 or option>7):
                print('Opción no válida. Intente de nuevo')
            else:
                if option == 1:
                    add_experiments(experiments)
                    '''experiments = []
                    experiment1 = Experiments('Exp1', 11/11/2024, 'Biología', [23,34,35,46,56])
                    experiment2 = Experiments('Exp2', 11/12/2025, 'Física', [23,2,4,65.56,5])
                    experiment3 = Experiments('Exp3', 11/10/2026, 'Química', [3.4,3,55.6,23,34.5])
                    experiments.append(experiment1)
                    experiments.append(experiment2)
                    experiments.append(experiment3)''' 
                elif option == 2:
                    visualize_experiments(experiments)
                elif option == 3:
                    calculate_experiments(experiments)
                elif option == 4:
                    compare_experiments(experiments)
                elif option == 5:
                    erase_experiments(experiments)
                elif option == 6:
                    generate_Report(experiments)
                elif option == 7:
                    print("Saliendo del programa. ¡Hasta luego!")
                    break
        except(ValueError):
            print("Opción no válida. Intente de nuevo.")

# Ejecución del programa
if __name__ == "__main__":
      # Llama al menú principal para iniciar la interacción
    menu()