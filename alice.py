from ca import *

def guardar(fichero,datos):
    file_out = open(fichero, "wb")
    file_out.write(datos)
    file_out.close()

cadena="Hola amigos de la seguridad"
carg_alice=cargar_RSAKey_Privada("alice.pem","P2SeguridadAlice")
carg_bob=cargar_RSAKey_Publica("bob.pub")
cifrado=cifrarRSA_OAEP(cadena,carg_bob)
#print("Cifrado:",cifrado)
guardar("./alice2cifrado.bin",cifrado)
firma=firmarRSA_PSS(cadena,carg_alice)
guardar("./alice2firma.bin",cifrado)

