from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pss
from Crypto.Hash import SHA256

def crear_RSAKey():
    key = RSA.generate(2048)
    return key

def guardar_RSAKey_Privada(fichero, key, password):
    key_cifrada = key.export_key(passphrase=password, pkcs=8, protection="scryptAndAES128-CBC")
    file_out = open(fichero, "wb")
    file_out.write(key_cifrada)
    file_out.close()

def cargar_RSAKey_Privada(fichero, password):
    key_cifrada = open(fichero, "rb").read()
    key = RSA.import_key(key_cifrada, passphrase=password)

    return key

def guardar_RSAKey_Publica(fichero, key):
    key_pub = key.publickey().export_key()
    file_out = open(fichero, "wb")
    file_out.write(key_pub)
    file_out.close()

def cargar_RSAKey_Publica(fichero):
    keyFile = open(fichero, "rb").read()
    key_pub = RSA.import_key(keyFile)

    return key_pub

def cifrarRSA_OAEP(cadena, key):
    datos = cadena.encode("utf-8")
    engineRSACifrado = PKCS1_OAEP.new(key)
    cifrado = engineRSACifrado.encrypt(datos)

    return cifrado

def descifrarRSA_OAEP(cifrado, key):
    engineRSADescifrado = PKCS1_OAEP.new(key)
    datos = engineRSADescifrado.decrypt(cifrado)
    cadena = datos.decode("utf-8")

    return cadena

def firmarRSA_PSS(texto, key_private):
    h = SHA256.new(texto.encode("utf-8")) # Crea un nuevo objeto SHA 256, pasándole el texto
    print(h.hexdigest()) # Muestra el hash del texto en hexadecimal (NOTA: prueba a poner print(h.digest()) en la siguiente línea...)
    signature = pss.new(key_private).sign(h)
    
    return signature

def comprobarRSA_PSS(texto, firma, key_public):
    h = SHA256.new(texto.encode("utf-8")) # Crea un nuevo objeto SHA 256, pasándole el texto
    print(h.hexdigest()) # Muestra el hash del texto en hexadecimal (NOTA: prueba a poner print(h.digest()) en la siguiente línea...)
    verifier = pss.new(key_public)
    try:
        verifier.verify(h, firma)
        return True
    except (ValueError, TypeError):
        return False


# # Crear clave RSA y guardar en ficheros la clave privada (protegida) y pública
# password = "password"
# private_file = "rsa_key.pem"
# public_file = "rsa_key.pub"

# # Crear la clave RSA y guardarla en ficheros
# key = crear_RSAKey()
# guardar_RSAKey_Privada(private_file, key, password)
# guardar_RSAKey_Publica(public_file, key)

# # Cargar las claves desde los ficheros
# RSA_private = cargar_RSAKey_Privada(private_file, password)
# RSA_public = cargar_RSAKey_Publica(public_file)

# # Cifrar y Descifrar con PKCS1 OAEP
# cadena = "Lo desconocido es lo contrario de lo conocido. Pasalo."
# cifrado = cifrarRSA_OAEP(cadena, RSA_public)
# print(cifrado)
# descifrado = descifrarRSA_OAEP(cifrado, RSA_private)
# print(descifrado)

# # Firmar y comprobar con PKCS PSS
# firma = firmarRSA_PSS(cadena, RSA_private)
# if comprobarRSA_PSS(cadena, firma, RSA_public):
#     print("La firma es válida")
# else:
#     print("La firma es inválida")
