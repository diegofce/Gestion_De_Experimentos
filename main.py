##          Dev Senior       27/11/2024 
## Reto 1 _ Python de Cero a Senior: 'La Ruta Maestra del Código'

##              Grupo #17
#   Cristhian Javier Garzón Jiménez C.C.1085938174
#   Diego Fernando Chacón Estacio C.C.1085941933

## PROYECTO DE INVESTIGACIÓN CIENTÍFICA EN PYTHON
 
import datetime 
from tabulate import tabulate  

# Se crea la clase Experimentos para instanciar objetos con atributos como: 
# Nombre del experimento, Fecha realización (DD/MM/AAAA), Tipo experimento y Resultados numéricos
class Experiments:
    # función de inicialización, recibe los atributos
    def __init__(self, nameExperiment, dateExperiment, typeExperiment, resultsExperiment):
        self.nameExperiment = nameExperiment
        self.dateExperiment = dateExperiment
        self.typeExperiment = typeExperiment
        self.resultsExperiment = resultsExperiment 
      
# Función para agregar experimentos: (permite al usuario crear nuevos experimentos con sus respectivos datos y se almacenan en una lista)
def add_experiments(experiments):
    nameExperiment = input("Ingrese el nombre del experimento: ")
    
    while True:                             
        # se valida que la fecha del experimento cumpla con el formato: DD/MM/AAAA
        dateExperiment_str = input("Ingrese la fecha de realización (ejm 23/11/2024): ")
        try:
            dateExperiment = datetime.datetime.strptime(dateExperiment_str, "%d/%m/%Y")
            break  
        except ValueError:
            print("Fecha no válida. Por favor, usar el formato DD/MM/AAAA")
    
    # se solicita al usuario escoger entre un listado de tipos de experimentos
    while True: 
        try:
            print('Experimentos disponibles:\n1. Biología \n2. Física \n3. Química')
            typeE = int(input('Seleccione el número de la categoría que desee: '))
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

    # se solicita al usuario que ingrese los resultados
    resultsExperiment = []
    cont = 0
    while True:
        try:
            result = float(input("Ingrese cada resultado numérico de su experimento: (ej: 4.5): "))
            if(result>=0):
                resultsExperiment.append(result)
                cont=cont+1     # se crea un contador de resultados
                print(f'---resultado #{cont} agregado con éxito---')
            else:
                print('** No se puede ingresar números negativos **')
            if(cont<3):
                print('Por favor ingrese mínimo 3 resultados')
            else:
                print('\n*** Si termino *** ==> Press enter')
        except ValueError:
            # Permite terminar la entrada de resultados
            if cont >= 3 and input("¿Terminar entrada de resultados? (Presione: (s) para salir): ").lower() == "s":
                break
            else:
                print('Debe ingresar al menos 3 resultados antes de finalizar.')

    if not resultsExperiment:  # Validar si la lista de resultados está vacía
        print("No se ingresaron resultados. El experimento no se guardará.")
        return
    
    # se almacenan los datos del experimento en un objeto instanciado de la Clase Experimentos
    experiment = Experiments(nameExperiment, dateExperiment, typeExperiment, resultsExperiment)
    experiments.append(experiment)

    print('\n\t--- Experimento agregado con éxito ---')

# funcion para visualizar experimentos: (permite al usuario visualizar los experimentos que ha agregado)
def visualize_experiments(experiments): 
    if not experiments:     # validación si no existen experimentos
        print("No hay experimentos registrados")
        return

    table = [
        [i+1, exp.nameExperiment, exp.dateExperiment.strftime('%d/%m/%Y'), exp.typeExperiment, exp.resultsExperiment]
        for i, exp in enumerate(experiments)
    ]
    print('')
    print(tabulate(table, headers=["#", "Nombre", "Fecha", "Tipo", "Resultados"]))

# funcion para calcular las estadisticas solicitadas:
# permite al usuario calcular estadísticas básicas (valor promedio, valor máximo y valor mínimo) de los resultados de los experimentos)
def calculate_experiments(experiments): 
    print('Experimentos disponibles para calcular estadísticas:')
    visualize_experiments(experiments)
    if not experiments:
        return
    try:
        # Solicitar al usuario que seleccione un experimento por número
        index = int(input("\nSeleccione el número del experimento a analizar: ")) - 1
        exp = experiments[index]
        results = exp.resultsExperiment
        if not results:
            print("El experimento seleccionado no tiene resultados.")
            return
        # Cálculos de estadísticas
        average = sum(results) / len(results)
        numMax = max(results)
        numMin = min(results)
        print(f"\nEstadísticas del experimento '{exp.nameExperiment}':")
        print(f"  Promedio: {average:.2f}, Máximo: {numMax:.2f}, Mínimo: {numMin:.2f}") #2 decimales
    except (IndexError, ValueError):
        print("Selección inválida.")

def compare_experiments(experiments):
    visualize_experiments(experiments)
    try:
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
            else:
                print(f'Indice {index+1} no válido')
        print('')
        for name, averageE, maxiE, minE in resultCompare:
            print(f'Nombre: {name}, Promedio: {averageE}, Maximo: {maxiE}, Mínimo: {minE}')
    except (ValueError):
        print('Entrada no válida, intente de nuevo')

def erase_experiments(experiments): #funcion para eliminar un experimento
    visualize_experiments(experiments)
    if not experiments:
        return
    try:
        index = int(input("\nSeleccione el número del experimento a eliminar: ")) - 1
        exp = experiments[index]
        print(f'Esta seguro que desea eliminar el experimento {exp.nameExperiment}?')
        conf = input('Si (s) _ No (n): ').lower()
        if(conf=='s' or conf=='si'):
            experiments.remove(exp)
            print('\n\t**Experimento eliminado con éxito**')
        else:
            print('No se eliminó ningún experimento')
            return
    except (IndexError,ValueError):
        print('Experimento no existente')

def generate_Report(experiments): #funcion para generar informe tipo resumen + Estadisticas
    """
    Crea un informe que incluye la descripción de todos los experimentos,
    sus resultados y estadísticas. Guarda el informe en un archivo .txt.
    """
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
    print(f"\nInforme generado con éxito, guardado como '{nameFile}'.")

    #"""
    #Muestra el menú principal con opciones para gestionar experimentos,
    #analizarlos, generar informes o salir del programa.
    #"""
def menu():
    experiments = []
    while True:
        try:
            print('\n|=======>  Menu:  <=======|')
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
                    print("\n\t--- Agregar Experimento ---")
                    add_experiments(experiments)
                elif option == 2:
                    print("\n\t--- Visualizar Experimentos ---")
                    visualize_experiments(experiments)
                elif option == 3:
                    print('\n\t--- Calcular Estadísticas ---')
                    calculate_experiments(experiments)
                elif option == 4:
                    print("\n\t--- Comparar Experimentos ---")
                    compare_experiments(experiments)
                elif option == 5:
                    print("\n\t--- Eliminar Experimentos ---")
                    erase_experiments(experiments)
                elif option == 6:
                    print("\n\t--- Generar Informe ---")
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