from alice import *

def leer(fichero):
    try:
        with open(fichero, 'rb') as file_in:  # Otwórz plik w trybie odczytu binarnego ('rb')
            data = file_in.read()  # Odczytaj dane z pliku
            return data
    except Exception as e:
        print(f"Failed to read data from {fichero}: {e}")
        return None

carg_bob=cargar_RSAKey_Privada("bob.pem","P2SeguridadBob")
carg_alice=cargar_RSAKey_Publica("alice.pub")
firma=leer("alice2firma.bin")
cifrado=leer("alice2cifrado.bin")
decifrado=descifrarRSA_OAEP(cifrado,carg_bob)
print(decifrado)
if comprobarRSA_PSS(decifrado,firma,carg_alice):
    print("La firma es válida")
else:
    print("La firma es inválida")



