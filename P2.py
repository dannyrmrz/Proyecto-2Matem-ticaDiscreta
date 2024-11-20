import random

def es_primo(num):
    #para ver si el número es primo
    if num <= 1:
        return False
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

def generar_primo(rango_inferior, rango_superior):
    #para generar un primo dentro de un rango especificado por el usuario
    primos = [num for num in range(rango_inferior, rango_superior) if es_primo(num)]
    if not primos:
        return None  #cuando no se encuentre un primo en el rango regresa "None"
    return random.choice(primos) 

def mcd(a, b):
    #para calcular el máximo común divisor de dos números con el algoritmo de euclides
    while b != 0:
        a, b = b, a % b
    return abs(a) #absoluto para que no regrese un número negativo

def inverso_modular(e, n):
    #para el inverso modular (el extendido de euclides)
    t, new_t = 0, 1
    r, new_r = n, e
    while new_r != 0:
        cociente = r // new_r
        t, new_t = new_t, t - cociente * new_t #t es actual y nt es el nuevo valor de t, igual para el de abajo, solo que con r
        r, new_r = new_r, r - cociente * new_r
    if r > 1:
        return None  #cuando no hay inverso modular regresa "None"
    if t < 0:
        t = t + n #para que el inverso sea positivo
    return t

'''
Genera las llaves pública y privada
1. Generar dos primos dentro de un rango especificado
2. Calcular el producto de los dos primos
3. Calcular el totiente de euler para asegurarse que los numeros sean coprimos de n
4. Generar un número aleatorio para e, que sea coprimo con phi
5. Generar el inverso modular de e y phi
6. Regresar las llaves pública y privada
'''
def generar_llaves(rango_inferior, rango_superiores):
    p = generar_primo(rango_inferior, rango_superiores)
    q = generar_primo(rango_inferior, rango_superiores) #Generar dos primos
    n = p * q #Calcular el producto de los dos primos
    phi = (p - 1) * (q - 1) #Calcular el totiente de euler para asegurarse que los numeros sean coprimos de n
    #Generar un número aleatorio para e, que sea coprimo con phi
    e = random.randint(1, phi)
    while mcd(e, phi) != 1: #Si son coprimos, se genera otro número aleatorio
        e = random.randint(1, phi)
    d = inverso_modular(e, phi) #Generar el inverso modular de e y phi
    if d is None:
        return None
    return (e, n), (d, n) #Regresar las llaves pública y privada

'''Cifra el mensaje con la llave pública
1. Convertir cada caracter a su valor ASCII con la función ord()
2. Elevar el valor ASCII a la potencia de e y n, 
3. Guardar el valor cifrado de cada caracter en una lista'''
def encriptar(mensaje, llave_publica): 
    e, n = llave_publica #Desempaquetar la llave pública
    mensaje_cifrado = [pow(ord(char), e, n) for char in mensaje]
    return mensaje_cifrado

'''Descifra el mensaje con la llave privada
1. Elevar cada valor cifrado a la potencia de d y n
2. Convertir el valor a su caracter correspondiente con la función chr()
3. Guardar el caracter descifrado en una lista'''
def desencriptar(mensaje_cifrado, llave_privada):
    d, n = llave_privada #Desempaquetar la llave privada
    mensaje_descifrado = [chr(pow(char, d, n)) for char in mensaje_cifrado]
    return ''.join(mensaje_descifrado) #Unir los caracteres descifrados en un solo string