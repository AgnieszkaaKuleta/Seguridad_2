from rsa import *

#alice
alice = crear_RSAKey()
guardar_RSAKey_Publica("./alice.pub", alice)
guardar_RSAKey_Privada("./alice.pem", alice, "P2SeguridadAlice")

#bob
bob = crear_RSAKey()
guardar_RSAKey_Publica("./bob.pub", bob)
guardar_RSAKey_Privada("./bob.pem", bob, "P2SeguridadBob")