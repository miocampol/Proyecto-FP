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
        regis_usuario_profes = open("registro usuario de profesores.txt", "a")
        regis_contra_profes = open("registro contrseña de profesores.txt", "a")
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
        regis_usuario_profes.write(usuario+"\n")
        regis_contra_profes.write(contraseña+"\n")
        regis_usuario_profes.close
        regis_contra_profes.close
        return regis_usuario_profes, regis_contra_profes
    

def registro_hecho(respu_uno_dos, archivo_usua, archivo_contra):
    if respu_uno_dos==1:
        usuario=input("Por favor digite su usuario: ")
        contraseña=input("Por favor digite su contrasseña: ")
        archivo_usua = open("registro usuario de profesores.txt", "r")
        archivo_contra = open("registro contrseña de profesores.txt", "r")
        lineas1 = archivo_usua.readlines()
        lineas2 = archivo_contra.readlines()
        for i in lineas1:
            if i == contraseña:
                print("la contraseña es correcta")
            else:
                print("su contraseña es incorrecta")
        for j in lineas2:
            if j == usuario:
                print("su usuario es correcto")
            else:
                print("su usuario es incorrecto")
            
            
uno_dos = estu_prof()
respu_uno_dos = pregunta_reg(uno_dos)
archivo_usua,archivo_contra=registro(respu_uno_dos)
registro_hecho(respu_uno_dos, archivo_usua, archivo_contra)


#nada=open(".txt","w")
#nada.write("migue"+"\n")
#nada.write("mundo")
#nada.close()
#nada = open("nada.txt", "r")
#lineas=nada.readlines()
#print(lineas[0])
    
