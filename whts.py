
## Evaluate user password program
password = input("Digite una contraseña :")
evaluate = input("Ahora debe introducir su contraseña :")
i = 1
while password != evaluate:
    if i < 3:
        i += 1
        evaluate = input((f"Contraseña incorrecta. Intentelo de nuevo ({i}/3 intentos restantes): "))
    else :
        print("Se excedio el máximo de intentos")
        break
if password == evaluate:
    print("La contraseña es correcta, puede continuar...")
