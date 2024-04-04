1. El código Python descrito en el apéndice A (y en las transparencias relacionadas con esta
práctica) muestra el funcionamiento del algoritmo RSA, junto con el funcionamiento de las
funciones Hash.
Utilizando dicho código como base, se pide realizar los siguientes ficheros con las siguientes
operaciones:
ca.py
a. Crear una clave pública y una clave privada RSA de 2048 bits para Alice. Guardar
cada clave en un fichero.
b. Crear una clave pública y una clave privada RSA de 2048 bits para Bob. Guardar
cada clave en un fichero.
alice.py
c. Cargar la clave privada de Alice y la clave pública de Bob.
d. Cifrar el texto “Hola amigos de la seguridad” utilizando la clave de Bob.
e. Firmar el texto “Hola amigos de la seguridad” utilizando la clave de Alice.
f. Guardar en unos ficheros, el texto cifrado y la firma digital1.
bob.py
g. Cargar la clave privada de Bob y la clave pública de Alice.
h. Cargar el texto cifrado y la firma digital.
i. Descifrar el texto cifrado y mostrarlo por pantalla.
j. Comprobar la validez de la firma digital.
2. La criptografía de curvas elípticas (o ECC) es una variante de la criptografía asimétrica basada
en las matemáticas de las curvas elípticas. Al igual que RSA, esta clase de criptografía permite
tanto realizar operaciones de cifrado2 como de firma.
Se pide implementar en el fichero ecc.py las funciones indicadas en el apéndice B utilizando
criptografía de curvas elípticas. Para ello, se deberá consultar la documentación de la librería
pycryptodome:
https://pycryptodome.readthedocs.io/en/latest/src/public_key/ecc.html
https://pycryptodome.readthedocs.io/en/latest/src/signature/dsa.html
3. (OPCIONAL) Usando como base el código del apartado 1 (RSA), crear un fichero
rsa_object.py que contenga una clase llamada RSA_OBJECT, la cual tenga los métodos
indicados en el apéndice C,
