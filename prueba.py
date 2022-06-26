from io import open
def estu_prof():
    pregunta = int(input("Por favor digite 1 sí es estudiante, o 2 sí es profesor: "))
    while pregunta < 1 or pregunta > 2:
        pregunta = int(input("El valor que está dando no es válido, digite 1 sí es estudiante, o 2 sí es profesor: "))
    return pregunta

def pregunta_reg(uno_dos):
    if uno_dos == 2:
        regis_log = int(input("Digite 1 sí ya está resgitrado, o digíte 2 sí aún no está registrado: "))
        while regis_log < 1 or regis_log > 2:
            regis_log = int(input("El valor que está dando no es válido, digite 1 sí ya está resgitrado, o digíte 2 sí aún no está registrado: "))
        return regis_log

def registro(respu_uno_dos):
    if respu_uno_dos == 2:
        regis_contra_profes = open("registro contrseña de profesores.txt", "a")
        regis_ususa_profes = open("registro ususario de profesores.txt", "a")
        print("INGRESE LOS SIGUIENTES DATOS PARA SU REGISTRO EN EL SISTEMA")
        nombre = input("Por favor ingrese su nombre: ")
        apellido = input("Por favor ingrese su apellido: ")
        correo = input("Por favor ingrese su correo: ")
        usuario = input("Por favor ingrese un usuario: ")
        contraseña = input("Por favor ingrese una contraseña: ")
        conf_contraseña = input("Vuelva a ingresar la contraseña: ")
        while contraseña != conf_contraseña:
            print("Las contraseñas no coinciden, por favor vuelva a ingresarlas")
            contraseña = input("Por favor ingrese una contraseña: ")
            conf_contraseña = input("Vuelva a ingresar la contraseña: ")
        print("Su registro ha sido correcto, ahora debe de hacer un log in para el ingreso al sistema")
        regis_ususa_profes.write(usuario+"\n")
        regis_contra_profes.write(contraseña+"\n")
        regis_ususa_profes.close
        regis_contra_profes.close
        return True

def registro_hecho(respu_uno_dos, si_registro):
    if respu_uno_dos == 1 or si_registro==True:
        print("HAGA EL LOG IN PARA EL INGRESO AL SISTEMA")
        nombre=input("Ingrese su nombre: ")
        usuario=input("Por favor ingrese su usuario: ")
        contraseña = input("Por favor digite su contrasseña: ")
        archivo_contra = open("registro contrseña de profesores.txt", "r")
        archivo_usua = open("registro ususario de profesores.txt", "r")
        lineas2 = archivo_usua.readlines()
        lineas = archivo_contra.readlines()
        if contraseña+"\n" in lineas and usuario+"\n" in lineas2:
            print("Sí está registrado")
            return True, nombre
        
        else:
            if contraseña+"\n" not in lineas:
                for i in range(3): 
                    contraseña = input("La contraseña es incorrecta o aún no se encuentra registrado, vuelva a ingresarla: ")
                    if contraseña+"\n" in lineas:
                        print("Sí está registrado")
                        return True, nombre
                print("No está registrado, por favor registrese")
            elif usuario+"\n" not in lineas2:
                for i in range(3):
                    usuario = input("El usuario es incorrecto o aún no se encuentra registrado, vuelva a ingresarlo: ")
                    if usuario+"\n" in lineas2:
                        print("Sí está registrado")
                        return True, nombre
                
                         
def ingreso_sistema(si_registro2, nombre):
    if si_registro2==True:
        print("Hola profe", nombre)
        
        
        
uno_dos = estu_prof()
respu_uno_dos = pregunta_reg(uno_dos)
si_registro = registro(respu_uno_dos)
si_registro2, nombre = registro_hecho(respu_uno_dos, si_registro)
ingreso_sistema(si_registro2, nombre)
