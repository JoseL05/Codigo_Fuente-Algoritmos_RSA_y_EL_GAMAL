#! /usr/bin/python
#Importar librerias necesarias
import numpy as np
from random import randint
import math
import hashlib
import argparse
import sys
import os
from time import time

parser =argparse.ArgumentParser(description='-------Algoritmo Elgamal-------')
#parser.add_argument('-cn',type=str)
parser.add_argument('-n',type=int,required=False,help="Numero a cifrar")
parser.add_argument('-out',type=str,required=False,help="Archivo cifrado de salida")
parser.add_argument('-ar',type=str,required=False,help="Archivo de entrada")
parser.add_argument('-m',type=str,required=False,help="Mensaje a cifrar")
parser.add_argument('-cn',action='store_true',help="Modalidad de cifrar un numero")
parser.add_argument('-cm',action='store_true',help="Modalidad de cifrar un mensaje")
parser.add_argument('-dn',action='store_true',help="Modalidad de descifrar numero")
parser.add_argument('-dm',action='store_true',help="Modalidad de descifrar un mensaje")
parser.add_argument('-fm',action='store_true',help="Firmar un documento")
parser.add_argument('-vf',action='store_true',help="Verificar una firma")
parser.add_argument('-gen',action='store_true',help="Generar valores")
parser.add_argument('-help',action='store_true',help="-help para desplegar ayuda completa!!!!!!!")
args = parser.parse_args()

#--------------generador de claves------------------

def calcular_primo():
    primo=False
    while primo==False:
        primo=True
        
        #--escoger un numero primo aleatorio grande--- 
        p1=randint(23000,25000)
        
        #---Validar si es un primo---
        for i in range(2, p1):
            if(p1%i)==0:
                primo=False
                break
            
        #if primo==True:
         #   print ("El numero",p1,"es primo")
        #else:
         #   print ("El numero",p1,"no es primo")

    return p1

#------------Hallar una raiz primitiva--------------

def calcular_raiz_primitiva(p_a):
    raicesp=np.zeros(p_a-1)
    raiz= False
    aleatorio=1

    while raiz==False:# mientras no encuentre la raiz hacer lo siguiente ...
        nosirve=False
        #aleatorio=randint(0,p_a-1)# Varia los numeros de prueva
        aleatorio= aleatorio+1
        for i in range(1,p_a):# varia las potencias de todo el conjunto p
            raicesp[i-1]=(aleatorio**i)%p_a
                    
        #Encontrar raices que sirve
        for j in range(1,len(raicesp)):
            
            if raicesp[0] == raicesp[j]: # si algun elemento es igual a otro, no sirve la raiz de prueba
                nosirve=True                
      
            if nosirve== False:# si despues de evaluar la raiz continua siendo falso nosirve entonces esa raiz es valida
                raiz=True
            else:
                raiz=False
        
    return raicesp,aleatorio


#----------Calcular el inverso(Euclides extendido)---------------

def inverso(p_b,N3):
    

    n=1000# numero de valores que se podrian guardar
    g=np.ones(n)
    g[0]=p_b
    g[1]=N3
    y=np.zeros(n)
    u=np.zeros(n)
    u[0]=1
    u[1]=0
    v=np.zeros(n)
    v[0]=0
    v[1]=1
    i=1

    while g[i] !=0:
        y[i+1]=int(g[i-1]/g[i])
        g[i+1]=g[i-1]-(y[i+1]*g[i])
        u[i+1]=u[i-1]-(y[i+1]*u[i])
        v[i+1]=v[i-1]-(y[i+1]*v[i])
        i=i+1

    if (v[i-1]<0):
        v[i-1]=v[i-1]+g[0];
    
    N4=int(v[i-1])
    return N4



def mhelp():  # Menu de ayuda general
    print("                                                     ")
    print("------------Algoritmo Elgamal------------            ")
    print("|                                                    ")
    print("|     Sintaxis : python3.7 Elgamal.py <opciones>       ")
    #print("|     Sintaxis 2: ./Elgamal.py <opciones>            ")
    print("|                                                    ")
    print("|                                                    ")
    print("|  <opciones>:                                       ")
    print("|        -cn:  Cifrar un numero usando el algoritmo ELGAMAL     ")
    print("|        -dn:  descifrar un numero usando el algoritmo ELGAMAL  ")
    print("|        -cm:  Cifrar un mensaje usando el algoritmo ELGAMAL    ")
    print("|        -dm:  Descifrar un mensaje usando el algoritmo ELGAMAL ")
    print("|        -fm:  Firmar un mensaje usando el algoritmo ELGAMAL    ")
    print("|        -vf:  Validar la firma de un mensaje usando el algoritmo ELGAMAL    ")
    print("|        -gen:  Generar nuevas llaves publicas y privadas    ")    
    print("|                                                    ")
    print("|                                                    ")
    print("|  Para consultar una opcion en especifico use la siguiente sintaxis:")
    print("|                                                   ")
    print("|  python3.7 Elgamal.py <opciones> -help               ")
    print("|                                                   ")
    print("|  Ejemplo: python Elgamal.py -cn -help             ")
    print("|                                                   ")
    print("|  Autor: Jonathan Rivas                            ")
    print("|  Correo:jonathan.rivas@uao.edu.co                 ")
    print("|                                                   ")
    print("|  Autor: Jose Luis Rodriguez                       ")
    print("|  Correo:jose_l.rodriguez@uao.edu.co               ")
    print("|                                                   ")
    print("|  Universidad Autonoma de Occidente                ")
    print("|  Santiago, de Cali                                ")
    print("|                                                   ")
    print("|  Certificados y firmas digitales                  ")
    print("|  Profesor: Siler Amador                           ")
    print("|  Elaborado el Sabado,8 de Junio del 2019          ")
    print("-----------------------------------------           ")
   
def mhelp1():  # Menu de ayuda especifica cifrando un numero
    print("                                                                       ")
    print("------------Cifrando un numero------------                             ")
    print("|                                                                      ")
    print("|     Sintaxis : python3.7 Elgamal.py -cn -n <Clave> -out <Salida>       ")
    #print("|     Sintaxis 2: ./Elgamal.py -cn -n <Clave> -out <Salida>            ")  
    print("|                                                                      ")
    print("|     <Clave>:numero a cifrar                                          ")
    print("|      ejemplo: 20000                                                  ")
    print("|     <Salida>: nombre del archivo de salida con el numero cifrado     ")
    print("|      nota: Los archivos de clave se guardan con la extencion .cif    ")
    print("|                                                                      ")
    print("|  Ejemplo:                                                            ")
    print("|        Elgamal.py -cn -n 1000 -out archivocifrado                    ")
    print("|                                                                      ")
    print("|  Recomendaciones:                                                    ")
    print("|     <Clave>: Debe ser un entero positivo, en lo posible menor a 23000")
    print("|                                                                      ")
    print("-----------------------------------------                              ")

def mhelp2(): # Menu de ayuda especifica descifrando un numero
    print("                                                                       ")
    print("------------Descifrando un numero------------                          ")
    print("|                                                                      ")
    print("|     Sintaxis : python3.7 Elgamal.py -dn -ar <archivocifrado>           ")
    #print("|     Sintaxis 2: ./Elgamal.py -dn -ar <archivocifrado>                ")
    print("|                                                                      ")
    print("|     <archivocifrado>:nombre del archivo cifrado                      ")
    print("|      ejemplo: archivocifrado.cif                                     ")
    print("|                                                                      ")
    print("|  Ejemplo:                                                            ")
    print("|        python3.7 Elgamal.py -dn -ar archivocifrado.cif                  ")
    print("|                                                                      ")
    print("|  Recomendaciones:                                                    ")
    print("|     *Siempre especificar el archivo que desea descifrar              ")
    print("|                                                                      ")
    print("-----------------------------------------                              ")
    
def mhelp3():   # Menu de ayuda especifica cifrando un mensaje
    print("                                                                       ")
    print("------------Cifrando un mensaje------------                            ")
    print("|                                                                      ")
    print("|     Sintaxis : python3.7 Elgamal.py -cm -m <Mensaje> -out <Salida>     ")
    #print("|     Sintaxis 2: ./Elgamal.py -cm -m <Mensaje> -out <Salida>          ")   
    print("|                                                                      ")
    print("|     <Clave>:mensaje a cifrar                                          ")
    print("|      ejemplo: HolaComoEstas?                                         ")
    print("|     <Salida>: nombre del archivo de salida con el numero cifrado     ")
    print("|      nota: Los archivos de clave se guardan con la extencion .cif    ")
    print("|                                                                      ")
    print("|  Ejemplo:                                                            ")
    print("|        python3.7 Elgamal.py -cm -m HolaComoEstas? -out archivocifrado   ")
    print("|                                                                      ")
    print("|  Recomendaciones:                                                    ")
    print("|     <Mensaje>: No debe contener el caracter espacio                  ")
    print("|                                                                      ")
    print("-----------------------------------------                              ")

def mhelp4():  # Menu de ayuda especifica descifrando un mensaje
    print("                                                                  ")
    print("------------Descifrando un mensaje------------                    ")
    print("|                                                                 ")
    print("|     Sintaxis 1: python3.7 Elgamal.py -dm -ar <archivocifrado>      ")
    #print("|     Sintaxis 2: ./Elgamal.py                                    ")
    print("|                                                                 ")
    print("|     <archivocifrado>:nombre del archivo cifrado                 ")
    print("|      ejemplo: archivocifrado.cif                                ")
    print("|                                                                 ")
    print("|  Ejemplo:                                                       ")
    print("|        python3.7 Elgamal.py -dm -ar archivocifrado.cif             ")
    print("|                                                                 ")
    print("|  Recomendaciones:                                               ")
    print("|     *Siempre especificar el archivo que desea descifrar         ")
    print("|                                                                 ")
    print("-----------------------------------------                         ")

    
def mhelp5():  # Menu de ayuda especifica Firmando un documento
    print("                                                              ")
    print("------------Firmando un documento------------                 ")
    print("|                                                             ")
    print("|     Sintaxis 1: python3.7 Elgamal.py -fm -ar <Archivo>         ")
    #print("|     Sintaxis 2: ./Elgamal.py                                ")
    print("|                                                             ")
    print("|     <Archivo>:Documento a firmar                            ")
    print("|      ejemplo: MobyDick.txt                                  ")
    print("|                                                             ")
    print("|  Ejemplo:                                                   ")
    print("|        python3.7 Elgamal.py -fm -ar MobyDick.txt               ")
    print("|                                                             ")
    print("|  Recomendaciones:                                           ")
    print("|     <Archivo>: En lo posible asegurese que el archivo       ")
    print("|                cargado no contenga espacios en su           ")
    print("|                nombre.                                      ")
    print("-----------------------------------------                     ")

def mhelp6():  # Menu de ayuda especifica validando la Firmando un documento
    print("                                                                   ")
    print("------------Validando la firma de un documento ------------        ")
    print("|                                                                  ")
    print("|     Sintaxis 1: python3.7 Elgamal.py -vf -ar <ArchivoPrueba>        ")
    #print("|     Sintaxis 2: ./Elgamal.py             ")
    print("|                                                                  ")
    print("|     <ArchivoPrueba>:nombre del archivo que se desea validar la firma ")
    print("|      ejemplo: ArchivoPrueba.txt                                  ")
    print("|                                                                  ")
    print("|  Ejemplo:                                                        ")
    print("|        python3.7 Elgamal.py -vf -ar ArchivoPrueba.txt               ")
    print("|                                                                  ")
    print("|  Recomendaciones:                                                ")
    print("|     *Siempre especificar el archivo que desea validar la firma   ")
    print("|                                                                  ")
    print("-----------------------------------------                          ")    

def mhelp7():  # Menu de ayuda especifica validando la Firmando un documento
    print("                                                                   ")
    print("------------Generando nuevas llaves publicas y privadas ------------        ")
    print("|                                                                  ")
    print("|     Sintaxis 1: python3.7 Elgamal.py -gen        ")
    #print("|     Sintaxis 2: ./Elgamal.py             ")
    print("|                                                                  ")
    print("|     ")
    print("|  Ejemplo:                                                        ")
    print("|        python3.7 Elgamal.py -gen              ")
    print("|                                                                  ")
    print("|  Recomendaciones:                                                ")
    print("|     *Generar nuevas llaves regularmente  ")
    print("|                                                                  ")
    print("-----------------------------------------                          ")    
        
def hallar_valores():
    
    #----------Generar de claves tanto de A como de B-------------
    p_a=calcular_primo()    
    raicesp,alpha_a=calcular_raiz_primitiva(p_a)
    
    #Escoger clave privada dentro del conjunto p_a
    lambda_a=randint(1,50)
    
    #Calcular la clave publica de A
    beta=(alpha_a**lambda_a)%p_a
    
    #para B
    p_b=calcular_primo()
    raicesp2,alpha_b=calcular_raiz_primitiva(p_b)
    
    #Escoger clave privada dentro del conjunto p_b
    lambda_b=randint(1,50)
    
    #---Calcular la clave publica-----
    beta2=(alpha_b**lambda_b)%p_b
    
    return p_a,raicesp,alpha_a,lambda_a,beta,p_b,raicesp2,alpha_b,lambda_b,beta2
    
def info_pub(p_a, alpha_a,beta,N1,N2):
    print("|      ")
    print("---Informacion publica generada ---")
    print("| El numero del cuerpo escogido es:",p_a)
   #print ("Conjunto de la raiz de prueba=",raicesp)
    print("| Raiz primitiva escogida=",alpha_a);
    print("| La clave publica es:",beta)
    print("| N1=",N1)
    print("| N2=",N2)
    print("|      ")
    print("|      ")
    
def hallar_eulerphi(p_a):
    eulerphi=0;

    for i in range(1,p_a):
        if math.gcd(i,p_a)==1:
            eulerphi=eulerphi+1
        
    print("| eulerphi:",eulerphi)
    valido=False
    while valido==False:
        valido=False
        H=randint(1,p_a);
        if math.gcd(H,eulerphi)==1:
            valido=True
    

    #print("| El numero H es:",H)
    #Calcular H^-1

    #-----Calcular el inverso---------
    H2=inverso(eulerphi,H)
    #print("| inverso del numero es:",H2)
    return H,H2,eulerphi
#----------------------Programa principal----------------------------
if __name__ == '__main__':
    
    
    #--------------------------------------------------------------
    #Funciones del programa
    
    if args.help and not args.cn and not args.dn and not args.cm and not args.dm and not args.fm and not args.vf and not args.gen:  #Ayuda
        mhelp()
        
    if args.cn and args.help: #Ayuda cifrando un numero
        args.n=0
        mhelp1()
        
    if args.dn and args.help: #Ayuda descifrando un numero
        mhelp2()
        
    if args.cm and args.help: #Ayuda cifrando un mensaje
        mhelp3()
        
    if args.dm and args.help: #Ayuda descifrando un mensaje
        mhelp4()
    
    if args.fm and args.help: #Ayuda Firmando un documento
        mhelp5()
        
    if args.vf and args.help: #Ayuda validando un documento
        mhelp6()
    
    if args.gen and args.help:#ayuda generando llaves
        mhelp7()
          
    if args.gen:
        p_a, raicesp, alpha_a, lambda_a, beta, p_b, raicesp2, alpha_b, lambda_b, beta2=hallar_valores()
        
        #Guardar archivo de claves publicas y privadas
        file = open("claves.key", "w")
        file.write(str(p_a) + os.linesep)
        file.write(str(raicesp) + os.linesep)
        file.write(str(alpha_a)+ os.linesep)
        file.write(str(lambda_a)+ os.linesep)
        file.write(str(beta)+ os.linesep)
        file.write(str(p_b)+ os.linesep)
        file.write(str(raicesp2)+ os.linesep)
        file.write(str(alpha_b)+ os.linesep)
        file.write(str(lambda_b)+ os.linesep)
        file.write(str(beta2))
        file.close()
        
    if args.cn and args.n>1 and not args.help:# cifrando numero
        start_time = time()# inicia el conteo del tiempo
        print("|          ")
        print("----Cifrando un numero----")
        print("|          ")
        print("| Calculando claves...          ")
        #p_a,raicesp,alpha_a,lambda_a,beta,p_b,raicesp2,alpha_b,lambda_b,beta2=hallar_valores()
        i=0
        claves=[0,0,0,0,0,0,0,0,0,0]
        file = open("claves.key", "r")
        
        for linea in file.readlines():
            claves[i]=linea
            i=i+1
        
        file.close()
        p_a=int(claves[0])
        raicesp=claves[1]
        alpha_a=int(claves[2])
        lambda_a=int(claves[3])
        beta=int(claves[4])
        p_b=int(claves[5])
        raicesp2=claves[6]
        alpha_b=int(claves[7])
        lambda_b=int(claves[8])
        beta2=int(claves[9])
        
        
        O=args.out
        N=args.n
        u=randint(1,100)
        N1= (alpha_b**u)%p_b
        N2=(N*(beta2**u))%p_b
        # Presentar informacion
        info_pub(p_a, alpha_a,beta,N1,N2)
        
        #Guardar archivo cifrafo
        file = open(O+".cif", "w")
        file.write(str(N1) + os.linesep)
        file.write(str(N2))
        file.close()
        
        #Imprimir tiempo de cifrado
        t = time() - start_time
        print("| Tiempo cifrando:",t)
        print("|          ")
        print("------------------------------")
    
        
        
    if args.cm and not args.help:# cifrando un mensaje
        start_time = time()# inicia el conteo del tiempo
        print("|          ")
        print("----Cifrando un mensaje----")
        print("|          ")
        print("| Calculando llaves...          ")
        #p_a,raicesp,alpha_a,lambda_a,beta,p_b,raicesp2,alpha_b,lambda_b,beta2=hallar_valores()
        i=0
        claves=[0,0,0,0,0,0,0,0,0,0]
        file = open("claves.key", "r")
        
        for linea in file.readlines():
            claves[i]=linea
            i=i+1
        
        file.close()
        p_a=int(claves[0])
        raicesp=claves[1]
        alpha_a=int(claves[2])
        lambda_a=int(claves[3])
        beta=int(claves[4])
        p_b=int(claves[5])
        raicesp2=claves[6]
        alpha_b=int(claves[7])
        lambda_b=int(claves[8])
        beta2=int(claves[9])
        
        
        
        mensaje= args.m
        tmensaje=len(mensaje)
        letras=[]
        for i in range(0,tmensaje):
            letras.append(mensaje[i])
        #print("tam=", tmensaje)
        #print("Caracteres separados:", letras)
        valordec=[]
        for i in range(0,tmensaje):
            valordec.append(ord(letras[i]))

        
        
        #Cifrando el mensaje
        print("| Cifrando el mensaje...         ")
        u=randint(1,100)
        N2=[]
        N1= (alpha_b**u)%p_b
        #print("N1=",N1)
        for i in range(0, tmensaje):
            N2.append(str((int(valordec[i])*(beta2**u))%p_b))
        
        
        #Guardar archivo cifrafo
        O=args.out
        print("| Archivo cifrado enviado con exito!         ")
        file = open(O+".cif", "w")
        file.write(str(N1) + os.linesep)
        for i in range (0,tmensaje):
            file.write(N2[i] + os.linesep)
    
        file.close()
        
        
        #Imprimir tiempo de cifrado
        t = time() - start_time
        print("| Tiempo cifrando:",t)
        print("|          ")
        print("------------------------------")
    
    if args.dn and not args.help:# Descifrando numero
        start_time = time()# inicia el conteo del tiempo
        print("|          ")
        print("----Descifrando un numero----")
        print("|          ")
        print("| Leyendo archivos...          ")
        
        i=0
        mensaje=[0,0]
        
        claves=[0,0,0,0,0,0,0,0,0,0]
        file = open("claves.key", "r")
        
        for linea in file.readlines():
            claves[i]=linea
            i=i+1
        
        file.close()
        p_a=int(claves[0])
        #raicesp=int(claves[1])
        alpha_a=int(claves[2])
        lambda_a=int(claves[3])
        beta=int(claves[4])
        p_b=int(claves[5])
        #raicesp2=int(claves[6])
        alpha_b=int(claves[7])
        lambda_b=int(claves[8])
        beta2=int(claves[9])
        
        i=0
        
        file = open(args.ar, "r")      # Leer tupla recibida por A
        #file = open("TuplaN1N2.cif","r")
        for linea in file.readlines():
            mensaje[i]=linea
            i=i+1
        
        file.close()    

        N1=int(mensaje[0])
        N2=int(mensaje[1])
        N3=(N1**lambda_b)%p_b
        #x=math.gcd(N3,p_b)
        N4=inverso(p_b,N3)
        N=(N2*N4)%p_b
        print("| Numero descifrado:",N)
        
        #Imprimir tiempo de cifrado
        t = time() - start_time
        print("| Tiempo descifrando:",t)
        print("|          ")
        print("------------------------------")
    
        
    if args.dm and not args.help: # decifrando mensaje
        start_time = time()# inicia el conteo del tiempo
        i=0
        claves=[0,0,0,0,0,0,0,0,0,0]
        file = open("claves.key", "r")
        
        for linea in file.readlines():
            claves[i]=linea
            i=i+1
        
        file.close()
        p_a=int(claves[0])
        raicesp=claves[1]
        alpha_a=int(claves[2])
        lambda_a=int(claves[3])
        beta=int(claves[4])
        p_b=int(claves[5])
        raicesp2=claves[6]
        alpha_b=int(claves[7])
        lambda_b=int(claves[8])
        beta2=int(claves[9])
        
        
        
        mensaje=[]
        file = open(args.ar, "r")      # Leer tupla recibida por A
        #file = open("TuplaN1N2.cif","r")
        for linea in file.readlines():
            mensaje.append(int(linea))
        
        file.close()    
        #print(mensaje)
        m=""
        #descifrando...
        N3=(mensaje[0]**lambda_b)%p_b
        N4=inverso(p_b,N3)
     
        for i in range(1, len(mensaje)):
            N=(mensaje[i]*N4)%p_b
            aux=chr(N)# decimal to ascii
            m=m+aux # concatenar valores 
            
        
        t = time() - start_time
        print("          ")
        print("----Descifrando el mensaje----")
        print("|          ")
        print("| Mensaje descifrado:",m)
        print("| Tiempo descifrando:",t)
        print("|          ")
        print("------------------------------")


    if args.fm and not args.help:#----- Firmando un documento-------
        start_time = time()# inicia el conteo del tiempo
        print("          ")
        print("--------Firmando  un documento--------")
        print("|          ")
        print("|           ")
        #leer el documento
        
        #archivo=open(args.ar,"r")
        archivo=open(args.ar,"r",encoding = "ISO-8859-1")
        
        mensaje=""
        for linea in archivo.readlines(): 
            mensaje=mensaje+linea

        archivo.close()
        #mensaje = bytes(mensaje, 'utf-8')
        mensaje = bytes(mensaje,'ISO-8859-1')
        
	#mensaje =bytes(mensaje)
       
        #Calcular el hash del documento
        hash_mensaje_md5= hashlib.md5(mensaje)
        print("| Hash del documento en md5:",hash_mensaje_md5.hexdigest())
        #hash_base10=int(hash_mensaje_md5.hexdigest(),16)
        #print("Hash en base 10:",hash_base10)
        
        #separar el hash
        h=hash_mensaje_md5.hexdigest()
        tam_hash=len(h)
        letras=[]
        for i in range(0,tam_hash):
            letras.append(h[i])
        #print("tam=", tam_hash)
        #print("Caracteres separados:", letras)

        valordec=[]
        for i in range(0,tam_hash): # de ascii a decimal
            valordec.append(ord(letras[i]))

        #print("valores decimales del mensaje:",valordec)
        
        #Calcular claves publicas
        print("| Calculando llaves...  ") 
        #p_a,raicesp,alpha_a,lambda_a,beta,p_b,raicesp2,alpha_b,lambda_b,beta2=hallar_valores()
        i=0
        claves=[0,0,0,0,0,0,0,0,0,0]
        file = open("claves.key", "r")
        
        for linea in file.readlines():
            claves[i]=linea
            i=i+1
        
        file.close()
        p_a=int(claves[0])
        #raicesp=int(claves[1])
        alpha_a=int(claves[2])
        lambda_a=int(claves[3])
        beta=int(claves[4])
        p_b=int(claves[5])
        #raicesp2=int(claves[6])
        alpha_b=int(claves[7])
        lambda_b=int(claves[8])
        beta2=int(claves[9])
        
        H,H2,eulerphi=hallar_eulerphi(p_a)
        
        #Hallar r y s


        r=(alpha_a**H)%p_a
        s=[]
        #Calcular s
        for i in range(0, tam_hash):
            s.append(((valordec[i]-(lambda_a*r))*H2)%eulerphi)

        #Guardar el hash
        
        file = open("hash.cif", "w")
        file.write(str(r) + os.linesep)
        for i in range (0,tam_hash):
            file.write(str(s[i]) + os.linesep)
    
        file.close()
        print("| Archivo hash.cif creado con exito! ")
        
        t = time() - start_time
        
        print("|          ")
        print("| Tiempo cifrando el hash:",t)
        print("|          ")
        print("---------------------------------------------")
        
        
    if args.vf and not args.help: # ----------Verificando firma---------
        start_time = time()# inicia el conteo del tiempo
        print("          ")
        print("----Verificando la firma de un documento----")
        print("|          ")
        print("|           ")
        
        i=0
        claves=[0,0,0,0,0,0,0,0,0,0]
        file = open("claves.key", "r")
        
        for linea in file.readlines():
            claves[i]=linea
            i=i+1
        
        file.close()
        p_a=int(claves[0])
        raicesp=claves[1]
        alpha_a=int(claves[2])
        lambda_a=int(claves[3])
        beta=int(claves[4])
        p_b=int(claves[5])
        raicesp2=claves[6]
        alpha_b=int(claves[7])
        lambda_b=int(claves[8])
        beta2=int(claves[9])
        
        
        #descifrando
        mensaje=[]
        file = open("hash.cif", "r")      
        for linea in file.readlines():
            mensaje.append(int(linea))
        
        file.close()    
    

        r=mensaje[0]
        N1=[]
        k1=[]
        m=""
        N2=(beta**r)%p_a     

        for i in range(1, len(mensaje)):
            N1.append((r**mensaje[i])%p_a)
            k1.append((N1[i-1]*N2)%p_a)

        k1total=0
        for i in range(0, len(k1)):
            k1total=k1[i]+ k1total
        
        #print("K1 total=",k1total)
        
        #---Leer el documuento recibido------
        
        archivo=open(args.ar,"r", encoding = "ISO-8859-1")
        mensaje=""
        for linea in archivo.readlines(): 
            mensaje=mensaje+linea

        archivo.close()
        mensaje = bytes(mensaje,'ISO-8859-1')

        #Calcular el hash del documento
        hash_mensaje_md5= hashlib.md5(mensaje)
        print("| Hash del documento recibido en md5:",hash_mensaje_md5.hexdigest())
        
        #separar el hash del mensaje
        h=hash_mensaje_md5.hexdigest()
        tam_hash=len(h)
        letras=[]
        for i in range(0,tam_hash):
            letras.append(h[i])
        

        valordec=[]
        for i in range(0,tam_hash): # de ascii a decimal
            valordec.append(ord(letras[i]))

        k2=[]
        for i in range(0, len(valordec)):
            k2.append((alpha_a**int(valordec[i]))%p_a)

        #print(k2)    
        k2total=0
        for i in range(0, len(k2)):
            k2total=k2[i]+ k2total    
    
        #print("K2 total=",k2total)
        if k1total==k2total:
            print("| Firma digital identica!!")
        else:
            print("| Firma digital Falsa!!")
        print("|          ")
        t = time() - start_time
        
        print("|          ")
        print("| Tiempo validando:",t)
        print("|          ")
        print("---------------------------------------------")
        #print("N1:",N1)            
        #print("k1:",k1)
        #print("K1TOTAL=",k1total)
    
    #print("El numero del cuerpo escogido es:",p_a)
    #print ("Conjunto de la raiz de prueba=",raicesp)
    #print("Raiz primitiva encontrada=",alpha_a);
    
    
    #print("La clave privada es:",lambda_a)

    
    #print("La clave publica es:",beta)
    
    
    #print("El numero del segundo cuerpo es:",p_b)
            
    #print ("Conjunto de la raiz de prueba=",raicesp2)
    #print("Raiz primitiva encontrada=",alpha_b);

    
    #print("La clave privada es:",lambda_b)

    
    #print("La clave publica es:",beta2)
