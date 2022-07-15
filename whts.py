clave = "makinola"
i = 1
claveusr = input("Ingrese su contraseña")
while claveusr != clave:
    if i < 3:
        i += 1
    else:
        print("Ha alcanzado el número máximo de intentos.")
    claveusr = input((f"Contraseña incorrecta. Intente nuevamente ({i}/3 intentos): "))
print("Contraseña correcta. Puede continuar.")


