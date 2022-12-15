from logic.Simulator import Simulator
from matplotlib import pyplot

def printAuthors():
    print("_____________________________________________________________\n")
    print("Laboratorio 1 - Electiva de Simulacion")
    print("Integrantes:")
    print("Rose Yesenia Campos Carvajal - 2020072817")
    print("Luis Diego Mora Aguilar - 2018147110")
    print("_____________________________________________________________\n\n")

def askValues():
    resultado = []
    invalidOption = True
    #Map to make the menu choosing easier, maping each option number with the sides of the dice
    optionsMap = {1:4, 2:6, 3:8, 4:12, 5:20}
    print("Por favor, ingrese los datos para la simulacion.\n")
    while invalidOption:
        try:
            print("Elija la cantidad de caras que desea en su dado poliedro regular:")
            print("1- 4 caras")
            print("2- 6 caras")
            print("3- 8 caras")
            print("4- 12 caras")
            print("5- 20 caras")
            option = int(input())
            if option < 1 or option > 5:
                raise InterruptedError()
            resultado.append(optionsMap[option])
            print("Numero de veces que se lanza el dado: ")
            resultado.append(int(input()))
            print("Numero de experimentos: ")
            resultado.append(int(input()))
            invalidOption = False
        except:
            print("\nRespuesta invalida, por favor ingrese solo numeros o una opcion del menu valida\n")
            resultado.clear()
            print(resultado)
    return resultado

#main driver
#All the credits
printAuthors()
#Ask for sides, quantity of dice rolls per turn and how many experiments
input = askValues()
#Just out Simulator logic object that contains all the logic
simulator = Simulator(pC=input[0], pN=input[1], pK=input[2])

#Simulation begins!
simulationHash = simulator.startSimulation()

listaX = []     #x-axis, all the sum values for each experiment
listaY = []     #y-axis, all the appearances for each sum value per experiment
#Create x-axis and y-axis for the bars plot
for key, value in simulationHash.items():
    listaX.append(key)
    listaY.append(value)

print("Eje X:\nSumatoria de valores por experimento\n\t", str(listaX))
print("Eje Y:\nApariciones de cada sumatoria:\n\t", str(listaY)) 

#Make the bar graph with the dictionary that comes from the Simulator with the amounts of appearances

# The number of times a number appears

def graficabarras():

    #colores = ["blue", "red", "green"]
    pyplot.title("Cantidad de veces que aparece un número")
    pyplot.bar(listaX,height=listaY)
    pyplot.ylabel("Todas las apariciones")
    pyplot.xlabel("Todas las sumatorias")
    #pyplot.show()
    pyplot.savefig("test.png")

graficabarras()




