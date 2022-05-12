from math import gcd
import string

abecedario = string.ascii_uppercase
puntuacion = string.punctuation
a = 17
b = 20

def Euclides(a, b):
    return 1 == gcd(a, b)

def InversoModularMultiplicativo(a, n):
    for i in range(1, n):
        if(((a % n)* (i % n)) % n == 1):
            return i
    return -1

def Encriptado(texto, a, b):
    if not Euclides(a, 26):
        print("Los valores tienen que ser coprimos")
    letras = list(texto.upper())
    texto_cifrado = []
    for i in letras:
        try:
            x = (a * abecedario.index(i) + b) % 26
            texto_cifrado.append(abecedario[x]) 
        except ValueError:
            if i in puntuacion:
                continue
            if i != " ":
                texto_cifrado.append(i)
    return "".join(texto_cifrado)

def Desencriptar(encriptado, a, b):
    if not Euclides(a, 26):
        print("Los valores tienen que se coprimos")
    letras = list(encriptado)
    texto_descifrado = []
    mim = InversoModularMultiplicativo(a, 26)
    for i in letras:
        try:
            y = abecedario.index(i)
            decifrado = mim * (y - b) % 26
            texto_descifrado.append(abecedario[decifrado])
        except ValueError:
            texto_descifrado.append(i)
    return "".join(texto_descifrado)

el_texto = "ELEMENTALMIQUERIDOWATSON"
TextCifrado = Encriptado(el_texto, a, b)
print(TextCifrado)
print("=====================================")
TextoDescifrado = Desencriptar(TextCifrado, a, b)
print(TextoDescifrado)
print("=====================================")
TextCifrado2 = "OKHFSNKFNWFCWJHSNCHQYWFSWF"
TextoDescifrado2 = Desencriptar(TextCifrado2, a, b)
print(TextoDescifrado2)
