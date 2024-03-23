from usuario import Usuario

def guardar_error(excepcion):
  with open("error.log", "a") as archivo_error:
    archivo_error.write(str(excepcion) + "\n")

def procesar_usuarion():
  with open("usuarios.txt", "r") as json_usuarios:
    for linea in json_usuarios:
      try:
        datos_usuario = eval(linea)
        usuario = Usuario(datos_usuario["nombre"], datos_usuario["apellido"], datos_usuario["email"], datos_usuario["genero"])
        print(f"Usuario creado: {usuario.nombre} {usuario.apellidos}, Email: {usuario.email}, Género: {usuario.genero}")
      except Exception as e:
        guardar_error(e)

procesar_usuarion()