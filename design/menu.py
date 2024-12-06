from logic.formula import hi

def design():
    print("Bienvedido al mejor sistema del mundo")
    print("     0. Atrás")
    print("     1.Deseas que nuestra maquina salude")
    opc = int(input("Ingrese un número: "))
    if(opc == 1):
        name = input("Ingrese su nombre: ")
        resultado = hi(name)
        print(resultado)
    return opc