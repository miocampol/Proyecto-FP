from io import open
def estu_prof():
    pregunta = int(input("Por favor digite 1 sí es estudiante o 2 sí es profesor: "))
    while pregunta < 1 or pregunta > 2:
        pregunta = int(input("El valor que ingresó no es válido. Intente de nuevo, digite 1 sí es estudiante o 2 sí es profesor: "))
    return pregunta
def respues_prof(uno_dos):
    if uno_dos==2:
        regis_log = int(input("Digite 1 sí ya está resgitrado o digite 2 sí aún no está registrado: "))
        while regis_log < 1 or regis_log > 2:
            regis_log = int(input("El valor que ingresó no es valido. Intente de nuevo; digite 1 sí ya está resgitrado o digite 2 sí aún no está registrado: "))
        return regis_log
def validacion(reg_log):
    if reg_log==2:
        print("INGRESE LOS SIGUIENTES DATOS PARA SU REGISTRO EN EL SISTEMA")
        nombre=input("Por favor ingrese su nombre: ")
        apellido=input("Por favor ingrese su apellido: ")
        correo = input("Por favor ingrese su correo: ")
        usuario = input("Por favor ingrese un usuario: ")
        contraseña = input("Por favor ingrese una contraseña: ")
        conf_contraseña = input("Confirme su contraseña: ")
        while contraseña != conf_contraseña:
            print("Las contraseñas no coinciden, por favor vuelva a ingresarlas")
            contraseña = input("Por favor ingrese una contraseña: ")
            conf_contraseña = input("Vuelva a ingresar la contraseña: ")
        print("Su registro ha sido correcto, ahora debe de hacer un log in para el ingreso al sistema")
        dicc_regis={"usuario": usuario, "contraseña": contraseña}
        return dicc_regis, True
def archivo_datos_prof(archivo_prof, datos_prof):
    archivo_prof.write((datos_prof))
    archivo_prof.close()
    return archivo_prof
def validacion_2(reg_log,login):
    if reg_log==1:
        while validacion==False:
            usuario=input('Ingrese su usuario: ')
            contraseña=input('Ingrese su contraseña: ')
            prueba = login.read()
            if usuario==prueba and contraseña==prueba:
                print('Ingresó correctamente al sistema')
                validacion=True
            else:
                print('Por favor ingrese un usuario existente o regístrese')
                validacion=False
        return validacion
        
uno_dos = estu_prof()
reg_log= respues_prof(uno_dos)
datos_prof,booleano=validacion(reg_log)
archivo_prof = open('datos_profesor.txt','w')
login=archivo_datos_prof(archivo_prof,datos_prof)
validacion_2(reg_log,login)
#def respues_est(uno_dos):
    #cedula=int(input('Ingrese su numero de cedula sin puntos: '))
    ##buscar la cedula en los archivos
    ##if cedula está en los archivos, mostrar el numero y las notas
    ##elif cedula no está, mostrar por pantalla “No se encuentra registrado"
    #return
