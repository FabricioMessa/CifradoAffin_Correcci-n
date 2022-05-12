## Trabajo Grupal - PermanenteC
Integrantes:
- Royer Diosdado Carcausto Choquehuanca
- Fabricio Arian Messa Mandujano

Buenos días/tardes/noches profesor, hacemos entrega de la correccion del Cifrado Affin - PermanenteC_ejercicio2.

# Cifrado Affin
Para el cifrado Affin utilizamos el algoritmo de Euclides y el inverso modular multiplicativo que explicaremos uno por uno a continuación

1. Algoritmo de Euclides
  Utilizamos el método gcd:
    - def Euclides(a, b):  --> la funcion 
    
      - return 1 == gcd(a, b)  --> el maximo comun divisor de los valor a y b que ingresaremos
2. Inverso Modular Multiplicativo
  -def InversoModularMultiplicativo(a, n):
  
    -for i in range(1, n):  --> hacemos un recorrido desde 1 hasta "n"
    
        -if(((a % n)* (i % n)) % n == 1):  --> aquí hacemos el procedimiento y probamos si es que algún número entre el 1 y "n" es igual a 1
        
            -return i  --> aquí se retorna el número que dio igual a 1
            
    -return -1 --> retornamos la función
    
3. Encriptar mensaje
 Aquí haremos el encriptado del mensaje utilizando los 2 puntos que vimos anteriormente
 def Encriptado(texto, a, b):  --> inicia la funcion y toma el texto y los valores "a"/"b"
  
    -if not Euclides(a, 26):  --> aquí decimos si es que los valores no son aceptados por el algoritmo de Euclides creado anteriormente
    
        -print("Los valores tienen que ser coprimos")
        
    -letras = list(texto.upper())  --> .upper() sirve por si el texto que ingresaron está en minúsculas, y lo agregremos a otra variable
    
    -texto_cifrado = []  --> acá se va a ir almacenando el cifrado que hagamos abajo
    
    -for i in letras:  --> hacemos un recorrido en el texto que ingresamos, letra por letra
    
        -try:
        
            -x = (a * abecedario.index(i) + b) % 26  --> acá hacemos la operación de cifrado junto con los indices del abecedario 
            
            -texto_cifrado.append(abecedario[x])  --> acada vamos colocando letra por letra
            
        -except ValueError:
        
            -if i in puntuacion:  --> por si hubiera algún signo de puntiación
            
                -continue
                
            -if i != " ":  --> por si hubiera espacios en blanco
            
                -texto_cifrado.append(i)
                
    -return "".join(texto_cifrado)  --> finalmente retorna el texto cifrado con la llave (a, b) que pasamos junto con el texto 

4. Descifrar el mensaje
 Aquí haremos el descifrado de los mensajes con ayuda del inverso modular multiplicativo creado anteriormente
  
  código:
  
    def Desencriptar(encriptado, a, b):  --> empieza la función con el texto encriptado y la llave que son "a" y "b"
    if not Euclides(a, 26):  --> mismo procedimiento que el anterior
        print("Los valores tienen que se coprimos")
    letras = list(encriptado)  --> colocamos el texto encriptado en otra variable
    texto_descifrado = []  --> creamos una variable donde guardará cada palabra en el orden correcto
    mim = InversoModularMultiplicativo(a, 26)  --> usamos la función del inverso modular multiplicativo anteriormente creado
    for i in letras:  --> recorremos el texto encriptado
        try:
            y = abecedario.index(i)  --> apunta a los índices del abecedario
            decifrado = mim * (y - b) % 26  --> aquí está la operación para descifrar, multiplicamos el modular inverso con cada indice del abecedario menos la llave "b" 
            texto_descifrado.append(abecedario[decifrado])  --> los vamos colocando en la variable que guarda el texto en orden correcto
        except ValueError:
            texto_descifrado.append(i) --> añade los indices por si no está cifrado
    return "".join(texto_descifrado) --> te retorna la lista con el texto descifrado 
   
    
    
    
    
    
    
    
    
    
    
