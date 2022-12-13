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
printAuthors()
input = askValues()
print(input)
simulator = Simulator(pC=5, pN=10, pK=100)
listaConteo= simulator.startSimulation()
"""
Formato JSON
{
    sumaDeNumeros(int): cantidadApariciones(int)
}
"""

stubSimulation = {
    7: 4,
    5: 2,
    1: 3,
    12: 6
}

#Hacer la grafica de barras con el diccionario que viene del Simulador con las cantidades 
# de apariciones


