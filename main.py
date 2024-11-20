from P2 import *

def main():
    print("=== Generación de claves RSA ===")
    rango_inferior = 1
    rango_superior = 100

    try:
        # Generar las llaves pública y privada
        resultado = generar_llaves(rango_inferior, rango_superior)
        if resultado is None:
            print("No se pudieron generar las llaves. Intenta con un rango diferente.")
            return
        
        llave_publica, llave_privada = resultado
        print(f"Llave pública: {llave_publica}")
        print(f"Llave privada: {llave_privada}")
    except ValueError as e:
        print(f"Error: {e}")
        return

    print("\n=== Cifrado y Descifrado ===")
    mensaje = input("Escribe el mensaje a cifrar: ")

    # Encriptar el mensaje
    mensaje_cifrado = encriptar(mensaje, llave_publica)
    print(f"Mensaje cifrado: {mensaje_cifrado}")

    # Desencriptar el mensaje
    mensaje_descifrado = desencriptar(mensaje_cifrado, llave_privada)
    print(f"Mensaje descifrado: {mensaje_descifrado}")

    # Verificar que el mensaje descifrado coincide con el original
    if mensaje == mensaje_descifrado:
        print("\nEl mensaje fue cifrado y descifrado correctamente.")
    else:
        print("\nHubo un error al descifrar el mensaje.")

if __name__ == "__main__":
    main()