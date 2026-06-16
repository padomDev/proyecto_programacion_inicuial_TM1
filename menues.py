from servicios import *

def menu_ingreso():

    while True:

        print("-------------------------------------------------------------------")
        print("                           1. Registrarse                 ")
        print("                            2. Loguarse                   ")
        print("-------------------------------------------------------------------")

        try:
            opcion = int(input("                        Ingtrese una opcion: "))
            print("-------------------------------------------------------------------")

            match opcion :

                case 1 :
                    usuario = input("                      Ingrese nombre de usuario: ")
                    print("-------------------------------------------------------------------")
                    contraseña = input("                        Ingrese contraseña: ")
                    print("-------------------------------------------------------------------")
                    confirm_contraseña = input("                Ingrese nuevamente la contraseña: ")
                    print("-------------------------------------------------------------------")
                    pregunta = elegir_pregunta()
                    respuesta = menu_pregunta(pregunta)
                    print("-------------------------------------------------------------------")
                    registro = validaciones_registro(
                        usuario, 
                        contraseña, 
                        confirm_contraseña, 
                        pregunta, 
                        respuesta
                        )
                    if registro != True:    
                        for mensaje in registro:
                            print(mensaje)
                            menu_ingreso()
                    else:
                        print("Registro realizado con exito, bienvenido al club")
                        menu_principal()

                case 2 :
                    usuario = input("Ingrese nombre de usuario: ")
                    contraseña = input("Ingrese contraseña: ")
                    pregunta = elegir_pregunta()
                    respuesta = menu_pregunta(pregunta)
                    logueo = validaciones_login(
                        usuario, 
                        contraseña, 
                        pregunta, 
                        respuesta
                        )
                    if logueo != True:    
                        for mensaje in registro:
                            print(mensaje)
                            menu_ingreso()
                    else:
                        print("Login realizado con exito, bienvenido al club")
                        menu_principal()

                case _ :
                    print("Opcion invalida")

        except ValueError:
            print("El valor ingresado debe ser un número")



def menu_pregunta(pregunta):

    while True:

        print("         ", pregunta["pregunta"])
        print("-------------------------------------------------------------------")
        print(pregunta["opcion 1"])
        print(pregunta["opcion 2"])
        print(pregunta["opcion 3"])
        print(pregunta["opcion 4"])
        print("-------------------------------------------------------------------")

        try:

            respuesta = str(input("                 Ingrese una respuesta: "))

            if respuesta not in ["A", "B", "C", "D"]:
                print("-------------------------------------------------------------------")
                print("                         Respuesta invalida")
                print("-------------------------------------------------------------------")
                menu_pregunta(pregunta)

            return respuesta
            
        except ValueError:
            print("Se debe ingresar una letra mayuscula de la A a la D")

def menu_principal():

    while True:

        print("-------------------------------------------------------------------")

