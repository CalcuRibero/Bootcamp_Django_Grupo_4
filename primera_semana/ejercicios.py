#%%
#Buscar el elemento en una lista (cadena, numero ...)
#e imprimir u posición, y si no se encuentra imprimir None.

from cgi import print_environ_usage


def buscarMiElemento(elem, lista):
    if not elem in lista:
        print(None)
    else:
        print( f"Mi elemeto: {elem}\n , Mi posicion: {lista.index(elem)}")
    
buscarMiElemento(1, ['pablo', 1, 3])
buscarMiElemento(18, ['pablo', 1, 3])

#%% 
# devolver el num max de una lista, todos los numeros
# deben ser positivos cuando se evaluen.

def myNumMax(myLista):
    maximo = max(myLista)
    minimo = min(myLista)
    if (-minimo) > (maximo):
        return (-minimo)
    return maximo

myNumMax([1, -2, 3])
myNumMax([1, -2, 3, -40])

#%% 
# Hacer calculadora que le pregunte al usuario que 
# operacion desea realizar y le pida dos numeros para
# las operaciones, divisiones no pueden ser por cero

def calculadora():
    print("==================")
    print("1: Suma\n 2: Resta\n 3: Multiplicacion\n 4: Division")
    print("==================")
    opcion = int(input("Ingrese su opcion: "))
    while(True):    
        if opcion not in range(1, 5):
            print("Opcion invalida")
            continue
        a = int(input("Ingrese el primer valor"))
        b = int(input("Ingrese el segundo valor"))
        if opcion == 1:
            return (a + b)
        if opcion == 2:
            return (a - b)
        if opcion == 3: 
            return (a*b)
        if opcion == 4:
            if b == 0:
                print("Calculo Ilegal")
                continue
            return (a/b)

calculadora()

#%%
# Buscar en una lista de nombres y en una lista de 
# numeros el elemento que mas cantidad de veces aparece
# , obtener el elemento y la catidad de veces que se 
# aparece

