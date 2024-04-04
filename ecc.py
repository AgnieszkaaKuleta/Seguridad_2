from Crypto.PublicKey import ECC
from Crypto.Hash import SHA256
from Crypto.Signature import DSS

# Ver https://pycryptodome.readthedocs.io/en/latest/src/public_key/ecc.html
# Ver https://pycryptodome.readthedocs.io/en/latest/src/signature/dsa.html 

def crear_ECCKey():
    # Use 'NIST P-256'
    key = ECC.generate(curve='p256')
    return key



def guardar_ECCKey_Privada(fichero, key, password):
    with open(fichero, "wt") as f:
        data = key.export_key(format='PEM',
                               passphrase=password,
                               protection='PBKDF2WithHMAC-SHA512AndAES256-CBC',
                               prot_params={'iteration_count':131072})
        f.write(data)

def cargar_ECCKey_Privada(fichero, password):
    f = open(fichero, "rt")
    key = ECC.import_key(f.read(), passphrase=password)
    return key

def guardar_ECCKey_Publica(fichero, key):
    f = open(fichero, "wt")
    f.write(key.public_key().export_key(format="PEM"))
    f.close()


def cargar_ECCKey_Publica(fichero):
    f = open(fichero, "rt")
    key_pub = ECC.import_key(f.read())
    return key_pub

# def cifrarECC_OAEP(cadena, key):
# El cifrado con ECC (ECIES) aun no está implementado
# Por lo tanto, no se puede implementar este método aun en la versión 3.9.7 
#    return cifrado

# def descifrarECC_OAEP(cifrado, key):
# El cifrado con ECC (ECIES) aun no está implementado
# Por lo tanto, no se puede implementar este método aun en la versión 3.9.7 
#    return cadena

def firmarECC_PSS(texto, key_private):
        h = SHA256.new(texto.encode("utf-8")) # Crea un nuevo objeto SHA 256, pasándole el texto
        print(h.hexdigest()) # Muestra el hash del texto en hexadecimal (NOTA: prueba a poner print(h.digest()) en la siguiente línea...)
        signature = DSS.new(key, 'fips-186-3').new(key_private).sign(h)
        return signature

def comprobarECC_PSS(texto, firma, key_public):
    h = SHA256.new(texto.encode("utf-8"))
    verifier = DSS.new(key_public, 'fips-186-3')
    try:
        verifier.verify(h, firma)
        return True
    except (ValueError, TypeError):
        return False
    

# Crear clave RSA y guardar en ficheros la clave privada (protegida) y pública
password = "password"
private_file = "ecc_key.pem"
public_file = "ecc_key.pub"

# # Crear la clave RSA y guardarla en ficheros
key = crear_ECCKey()
guardar_ECCKey_Privada(private_file, key, password)
guardar_ECCKey_Publica(public_file, key)

# # Cargar las claves desde los ficheros


#RSA_private = cargar_RSAKey_Privada(private_file, password)RSA_public = cargar_RSAKey_Publica(public_file)

# # Cifrar y Descifrar con PKCS1 OAEP

#cadena = "Lo desconocido es lo contrario de lo conocido. Pasalo."
#cifrado = cifrarRSA_OAEP(cadena, RSA_public)
#print(cifrado)
#descifrado = descifrarRSA_OAEP(cifrado, RSA_private)
#print(descifrado)

# # Firmar y comprobar con PKCS PSS
# firma = firmarRSA_PSS(cadena, RSA_private)
# if comprobarRSA_PSS(cadena, firma, RSA_public):
#     print("La firma es válida")
# else:
#     print("La firma es inválida")