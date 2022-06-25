from io import open
archivo= open('ejemplo.txt','w')
numero=6
for i in range(10+1):
    multiplicar=numero*i
    archivo.write(f'\n{numero}*{i}={multiplicar}')
archivo.close()
