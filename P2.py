import random

def es_primo(num):
    #para ver si el número es primo
    if num < 2:
        return False
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

def generar_primo(rango_inferior, rango_superior):
    #para generar un primo dentro de un rango especificado por el usuario
    primo = [num for num in range(rango_inferior, rango_superior + 1) if es_primo(num)] #+1 para que no excluya el valor superior
    if not primo:
        return None  #cuando no se encuentre un primo en el rango regresa "None"
    return random.choice(primo) 

def mcd(a, b):
    #para calcular el máximo común divisor de dos números con el algoritmo de euclides
    while b != 0:
        a, b = b, a % b
    return abs(a) #absoluto para que no regrese un número negativo

def inverso_modular(e, n):
    #para el inverso modular (el extendido de euclides)
    t, nt = 0, 1
    r, nr = n, e
    while nr != 0:
        cociente = r // nr
        t, nt = nt, t - cociente * nt #t es actual y nt es el nuevo valor de t, igual para el de abajo, solo que con r
        r, nr = nr, r - cociente * nr
    if r > 1:
        return None  #cuando no hay inverso modular regresa "None"
    if t < 0:
        t = t + n #para que el inverso sea positivo
    return t