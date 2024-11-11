id = 1245
clave = 345
cuenta = 2000
opc = 0

def ver_edo():
    print(f"\nSu saldo es: {cuenta}")

def dep():
    global cuenta
    cant = float(input('\nIngrese monto: '))
    cuenta += cant
    ver_edo()

def ret():
    global cuenta
    cant_ret = float(input('\nIngrese el monto a retirar: '))
    if cant_ret > cuenta:
        print("\nSaldo insuficiente")
    else:
        cuenta -= cant_ret
        ver_edo()

try:
    key = int(input("Introduzca la clave: "))
    print("Clave: ", int(float(key)))
    if (key == clave):
        while opc != 4:
            opc = int ( input('''
                Seleccione la operación:
                    1. Edo. cuenta
                    2. Depósito
                    3. Retiro
                    4. Salir
                ''')
                )
            if opc == 1:
                ver_edo()
            elif opc == 2:
                dep()
            elif opc == 3:
                ret()
            elif opc == 4:
                print("Saliendo :)")
            else:
                print('\nOpción invalida!')
except:
    print('Información inválida!')