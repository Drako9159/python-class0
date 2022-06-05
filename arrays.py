#Arrays
arry = [1, 2, 3, 4, 5]
arry.append(0) # .append agrega algo a la lista
print(arry)
arry.extend(arry) # a.extend añade o duplica la lista 
print(arry)

arry = arry[::-1]
print(arry) # invertir la lista

arry.reverse()
print(arry) # .reverse también regresa la lista

arry.insert(0, 10) # .insert inserta elementos en una posición expesifica
print(arry)

arry.remove(10) # Elimina elementos de la lista
print(arry)
 

print(arry.pop(11)) # Retoma un elemento de una posición
print(arry) # Lo elimina e imprime

print(arry.count(1)) # Cuenta las veces que aparece un elemento

print(arry.index(4)) # Devuelve la posición de elemento dado
print(arry.index(5))

arry.sort() # Ordena la lista
print(arry)

arry.sort(reverse=True) # Ordena la lista al reves
print(arry)

arry2 = arry.copy() # Copia superficial de una lista
print(arry2)

arry.clear() # Limpia la lista
print(arry)

arry2 = [] # Limpia o crea la lista vacia
print(arry2)

