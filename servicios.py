#   Librerias importadas
import random

#   Lista de usuarios registrados.
usuarios = []

#   Lista con las contraseñas hasheadas de los usuarios registrados.
contraseñas_hasheadas = []

#   Lista de salts para los hasheos.
salts = []

#   Acumulador de mensajes de error para retornar al usuario.
mensaje_error = []

#   Funcion que sirve para validar las credenciales ingresadas por el usuario para su registro.
def validaciones_registro(
    usuario, 
    contraseña,
    confirm_contraseña,
    pregunta, 
    respuesta
    ):

    #   Valida que el nombre de usuario no se encuentre ya registrado.
    if usuario is usuarios:
        mensaje_error.append("Este nombnre de usuario ya esta registrado")

    #   Valida que el nombre de usuario tenga entre 6 y 50 caracteres.
    if len(usuario) < 6 or len(usuario) > 50:
        mensaje_error.append("      El nombre de usuario debe tener entre 6 caracteres y 50")

    #   Valida que el nomnre del usuario tenga al menos una letra mayuscula.
    if not any(letra.isupper() for letra in usuario):
        mensaje_error.append("El nomnre de usuairo debe contener al menos una letra mayuscula")

    #   Valida que el nombre del ususario tenga al menos un numero.
    if not any(letra.isdigit() for letra in usuario):
        mensaje_error.append("El nombre de usuario debe contener al menos un número")

    #   Valida que la contraseña tenga entre 6 y 50 caracteres.
    if len(contraseña) < 6 or len(contraseña) > 50:
        mensaje_error.append("La contraseña debe tener entre 6 caracteres y 50")
    
    #   Valida que las contraseñas coincidan.
    if contraseña != confirm_contraseña:
        mensaje_error.append("Las contraseñas no coinciden")
    
    #   Valida que la contraseña tenga al menos una letra mayuscula.
    if not any(letra.isupper() for letra in contraseña):
        mensaje_error.append("La contraseña debe contener al menos una letra mayuscula")

    #   Valida que la contraseña tenga al menos un numero.
    if not any(letra.isdigit() for letra in contraseña):
        mensaje_error.append("La contraseña debe contener al menos un número")

    #   Valida que la respuesta a la pregunta de ingreso sea correcta.
    if respuesta != pregunta["respuesta_correcta"]:
         mensaje_error.append("Respuesta ingresada incorrecta")
    
    #   Evalua si existen menmsajes de error. Si existen, los retorna y limpia el registro de errores.
    if mensaje_error:
        errores = mensaje_error.copy()
        mensaje_error.clear()
        return errores
    #   Si no hay errores, registra el usuario. Guarda su contraseña hasheada con salt, el salt lo guarda para poder validar ingresos futuros.
    else:
        usuarios.append(usuario)
        contraseña_hasheada = hash_casero_16_bytes(contraseña)
        contraseñas_hasheadas.append(contraseña_hasheada[0])
        salts.append(contraseña_hasheada[1])
        return True

#   Funcion para validar ingreso.
def validaciones_login(
    usuario,
    contraseña,
    pregunta, 
    respuesta
    ):
    #   Evalua que la respuesta del captcha sea correcta
    if respuesta == pregunta["respuesta_correcta"]:
    #   Busca el usuario en la lista de usuarios.
        posicion = buscar_usuario(usuarios, usuario, 0)
        #   Evalua si el usuario ingresado existe.
        if posicion != -1:
            #   Si existe, trae su contrasena hasheada utilizando la posicion del nombre de usuario en la lista de usuarios(porque la posicion del nombre de usuario y de su contraseña son las mimsmas en ambas listas).
            contraseña_hasheada_real = contraseñas_hasheadas[posicion]
            #   Tambien trar el salt que uso para hashear la contraseña usando la misma logica.
            salt = salts[posicion]
            #   Prepara la contrasena igresada por el usuario para compararla con la contraseña guardada en el registro.
            contraseña_hasheada = hash_casero_16_bytes_login(contraseña, salt)
            #   Evalua que ambas contraseñas sean iguales.
            if contraseña_hasheada[0] == contraseña_hasheada_real:
                #   Si lo son, la funcion retorna "True".
                return True
            #   Si no son iguales carga mensaje de error en la lista de errores.
            else:
                mensaje_error.append("La contraseña ingresada no coincide, pruebe nuevamente")
        #   Si el nombre de usuario no conidie lo carga en la lista de errores.
        else:
            mensaje_error.append("El nombre de usuario es incorrecto")
    #   Si la respuesta es incorrecta la carga en la lista de errores.        
    else:
        mensaje_error.append("Respuesta ingresada incorrecta")

    #   Retorna la lista de errores.
    errores = mensaje_error.copy()
    mensaje_error.clear()
    return errores

#   Funcion recursiva para buscar usuarios, esta funcion recibe una lista, un usuario y una posicion.
def buscar_usuario(
    lista, 
    usuario_buscado, 
    posicion
    ):

    #   Si la posicion brindada es mayor al numero maximo de posiciones en la lista, le resta 1.
    if posicion >= len(lista):
        return -1
    
    #   Si el elemento que se encuentra, dentro de la lista, en la posicion brindada es igual el nombre del usuario brindado, retorna la posicion en la lista de ese usuario.
    if lista[posicion] == usuario_buscado:
        return posicion
    
    #   Si ninguna de las dos cosas pasa, vuelve a ejecutrase sumando 1 a la ultima posicion evaluada.
    return buscar_usuario(
        lista, 
        usuario_buscado, 
        posicion + 1
        )

#   Esta funcion sirve para generar un cadena de 16 caracteres al azar
def salt_casero(largo=16):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    salt = ""

    #   Realiza 16 iteraciones sobre la lista de caracteres y en cada una guarda uno al azar.
    for i in range(largo):
        posicion = random.randint(0, len(caracteres) - 1)
        salt += caracteres[posicion]

    return salt

#   Esta funcion sirve para convertir la contraseña que ingresa el usuario en 
def hash_casero_16_bytes(contraseña):

    #   
    salt = salt_casero()

    #   Crea una lista de 16 números usando el salt
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

def hash_casero_16_bytes_login(contraseña, salt):

    #   Crea una lista de 16 números usando el salt
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


def elegir_pregunta():

    preguntas = [
        {
            "pregunta": "               ¿Qué es un firewall?",
            "opcion 1": "A) Un programa para editar imágenes",
            "opcion 2": "B) Una barrera que filtra tráfico de red",
            "opcion 3": "C) Un virus informático",
            "opcion 4": "D) Un tipo de memoria RAM",
            "respuesta_correcta": "B"
        },

        {
            "pregunta": "¿Para qué sirve el hashing de contraseñas?",
            "opcion 1": "A) Para guardar la contraseña en texto claro",
            "opcion 2": "B) Para convertir la contraseña en un valor no reversible",
            "opcion 3": "C) Para hacer la contraseña más corta",
            "opcion 4": "D) Para enviarla por email",
            "respuesta_correcta": "B"
        },

        {
            "pregunta": "¿Qué es un salt en hashing de contraseñas?",
            "opcion 1": "A) Un dato aleatorio que se suma antes de hashear",
            "opcion 2": "B) Una contraseña temporal",
            "opcion 3": "C) Un tipo de virus",
            "opcion 4": "D) Una copia de seguridad",
            "respuesta_correcta": "A"
        },

        {
            "pregunta": "       ¿Qué significa phishing?",
            "opcion 1": "A) Un ataque para engañar al usuario y robar información",
            "opcion 2": "B) Un tipo de antivirus",
            "opcion 3": "C) Una forma de comprimir archivos",
            "opcion 4": "D) Un protocolo de red",
            "respuesta_correcta": "A"
        }
    ]

    pregunta_actual = random.choice(preguntas)

    return pregunta_actual


