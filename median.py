

'''
**Las listas deben estar ordenadas de menor a mayor

Mediana en una lista con un numero inpar de numeros = numero en medio de la lista
Mediana en una lista con un numero par de números = la media de los dos numeros centrales

Ej.
[3, 1, 2, 5, 3] -> Mediana = 3
[1, 300, 2, 200, 1] --> Mediana = 2

'''

def mediana (array):
    # Calcular la mediana de un array de numeros
    median = None
    
    array.sort()
    
    length = len(data)
    
    if length%2!=0:
        median = array[length/2]
        
    else:
        median = (array[length/2] + data[length/2 - 1])/2.0
    
    return median
​
