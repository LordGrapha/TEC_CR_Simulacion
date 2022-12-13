from logic.Simulator import Simulator


def printAuthors():
    print("Laboratorio 1 - Electiva de Simulacion")
    print("Integrantes:")
    print("Rose Yesenia Campos Carvajal - 2020072817")
    print("Luis Diego Mora Aguilar - 2018147110")

def askValues():
    resultado = []
    print("C = Caras: ")
    resultado.append(int(input()))
    print("N = Numero de veces que se lanza el dado: ")
    resultado.append(int(input()))
    print("K = Experimentos: ")
    resultado.append(int(input()))
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


#Hacer la grafica de barras con el diccionario que viene del Simulador con las cantidades 
# de apariciones
