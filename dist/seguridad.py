#   Librerias importadas
import random

#   Esta funcion sirve para generar un cadena de 16 caracteres al azar
def salt_casero(largo=16):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    salt = ""

    #   Realiza 16 iteraciones sobre la lista de caracteres y en cada una guarda uno al azar.
    for i in range(largo):
        posicion = random.randint(0, len(caracteres) - 1)
        salt += caracteres[posicion]

    return salt

#   Esta funcion sirve para convertir la contraseña que ingresa el usuario en una cadena de caracteres unica.
def hash_casero_16_bytes(contraseña):

    #   Crea un salt especifico para cada hasheo
    salt = salt_casero()

    #   Crea una lista de 16 números usando el salt
    hash_bytes = []

    #   Convierte cada caracter del salta a su numero correspondiente en la tabla ascii
    for caracter in salt:
        hash_bytes.append(ord(caracter) % 256)

    #   Itera sobre cada caracter y su indeice en la contrasena ingresada por el usuario.
    for i, caracter in enumerate(contraseña):

        #   Convierte el caracter a su numero correspodniete en la tabla ascii
        numero = ord(caracter)

        #   Itera 16 veces, generando un caracter aleatorio utilizando el salt para cada caracter de la contraseña, devuelve siempre 16 caracteres independientemente del largo de la contraseña ingresada.
        for j in range(16):
            numero_salt = ord(salt[j])
            hash_bytes[j] = (
                hash_bytes[j] *  71
                + numero * (j+1)
                + numero_salt * (j+1)
                + i * 17
                + j * 13
            )%256
    
    #   Retorna la contrasena hasheada en formato haxadecimal de 16 bytes y el salt que se uso para hashear la contraseña.
    return bytes(hash_bytes).hex(), salt

#   Esta funcion es practiamente igual que la otra solo que en vez de crear el salt utiliza el que el usario utilizo para registrarse.
def hash_casero_16_bytes_login(contraseña, salt):

    hash_bytes = []

    for caracter in salt:
        hash_bytes.append(ord(caracter) % 256)

    for i, caracter in enumerate(contraseña):
        numero = ord(caracter)

        for j in range(16):
            numero_salt = ord(salt[j])
            hash_bytes[j] = (
                hash_bytes[j] *  71
                + numero * (j+1)
                + numero_salt * (j+1)
                + i * 17
                + j * 13
            )%256
    return bytes(hash_bytes).hex(), salt


