# String 
name = "Drako 🌝"
print(name)
# int
edad = 25
print(edad + edad)
# float
pi = 3.1416
#Transforma a otra variable (casteo)
edad = float(edad)
#Type para saber el tipo de variable
print(type(name),type(edad))
#Bool
tegusta = True
legustas = False
print(tegusta , legustas)
##Conditionals

calification = input("Introduce tu calificación ")
calification = int(calification)
if calification < 700 : 
    print("Ves por no estudiar")
elif calification > 700 :
    print("No puedes sacar más de 700")
else : print("A perro, ¡pasaste!")
# Verificador de mayoría de edad, implemente and or && ||
edad = input("Introduce tu edad ")
edad = int(edad)
if edad >= 18 and edad <= 100 :
    print("Bienvenido al mamitas")
elif edad > 100 :
    print("Si vienes acompañado de tus abuelos te fiamos")
elif edad <= 0 :
    print("Ni que fueras viejero del tiempo")
else : print("No puedes llevarte esos cigarros")
#arrays
listas = [1, 2, 3, 4, 5]
#functions
def funcion(nombre) :
    print(nombre)
funcion("jesus")

