#encoding:UTF-8
#Lenin Silva Gutiérrez
#Interpreta diálogo para dibujar

from Graphics import *
from Myro import pickAFile

def crearVentana(lista):#Recibe como parametro una lista
    #Las características de la ventana dependen de los elementos contenidos en la lista
    v = Window(lista[3],int(lista[1]), int(lista[2]))
    if len(lista)>4:
        v.setBackground(Color(lista[4])) #Elige 
    return v #Regresa la ventana para que otas funciones la puedan usar

def dibujarRectangulo(lista,ventana): #Recibe como parámetros una lista y la ventana
    #Las características del rectángulo dependen de los elementos en la lista
    rect = Rectangle((int(lista[1]),int(lista[2])),(int(lista[3]),int(lista[4])))
    #Determina si existe el parámetro para determinar color de relleno
    if len(lista)>5:
        rect.fill = Color(lista[5])
    else:
        rect.fill = Color(0,0,0,0)
    rect.draw(ventana) #Dibuja el rectángulo en la ventana
        
def dibujarCirculo(lista,ventana): #Recibe como parámetros una lista y la ventana 
    #Las características del círculo dependen de los elementos en la lista  
    circ = Circle((int(lista[1]),int(lista[2])),int(lista[3]))
    #Determina si existe el parámetro para determinar color de relleno 
    if len(lista)>4:
        circ.fill = Color(lista[4])
    else:
        circ.fill = Color(0,0,0,0)
    circ.draw(ventana)#Dibuja el círculo en la ventana 
    
def dibujarLinea(lista,ventana): #Recibe como parámetros una lista y la ventana 
    #Las características de la línea dependen de los elementos en la lista  
    linea = Line((int(lista[1]),int(lista[2])),(int(lista[3]),int(lista[4])))
    #Determina si existe el parámetro para determinar color de la línea
    if len(lista)>5:
        linea.color = Color(lista[5])
    linea.draw(ventana) #Dibuja la línea en la ventana 

def main():
    archivo = pickAFile() #El usuario selecciona el archivo que se abrirá
    for linea in file(archivo): #La variable 'linea' para cada iteración será una línea del archivo
        lista = linea.split() #Crea una lista a partir de la línea del archivo, separada por comas
        #print(lista)
        if len(lista)!=0: #Ignora líneas vacías
            #Determina qué tipo de acción se ejecutará
            clave = lista[0]
            if clave == "v":
               ventana = crearVentana(lista) #Permite usar la ventana para otras funciones
            elif clave == "r":
                dibujarRectangulo(lista, ventana)
            elif clave == "c":
                dibujarCirculo(lista, ventana)
            elif clave == "l":
                dibujarLinea(lista, ventana)
            
main()