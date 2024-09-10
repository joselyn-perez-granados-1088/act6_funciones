print("Mas sobre funciones")
#AQUI SE ESCRIBEN LAS FUNCIONES

#suma
def suma_ab(a,b):
    s=a+b
    return s
#resta
def resta_ab(a,b):
    s=a-b
    return s
#multiplicacion
def multi_ab(a,b):
    s=a*b
    return s
#division
def div_ab(a,b):
    s=a/b
    return s

#LLAMADAS A LA FUNCION
N1= int (input("ingresa el primer numero"))
N2=int (input("ingresa el segundo numero"))
suma=suma_ab(N1,N2)
print(f"la suma de {N1}+{N2}es: {suma}")

print(f"calculando resta")
N3= int (input("ingresa el primer numero"))
N4=int (input("ingresa el segundo numero"))
resta=resta_ab(N3,N4)
print(f"la suma de {N3}+{N4}es: {resta}")

print(f"calculando multiplicacion")
N5= int (input("ingresa el primer numero"))
N6=int (input("ingresa el segundo numero"))
multi=multi_ab(N5,N6)
print(f"la suma de {N5}+{N6}es: {multi}")

print(f"calculando division")
N7= int (input("ingresa el primer numero"))
N8=int (input("ingresa el segundo numero"))
division=div_ab(N1,N2)
print(f"la suma de {N7}+{N8}es: {division}")
