#INICIO
#importando librerías
import random
import pandas as pd
import numpy as np
etiquetas = ['Nombre','Tipo de servicio','Zona','Tiempo de servicio','Costo']
nombre = []
tipo = []
zona = []
tiempo= []
costo = []
for i in range (20):
     nombre.append('Nombre_'+str(random.randint(1000,9999)))
     tipo.append(random.choice(['telefonía','cable tv','internet']))
     zona.append(random.choice(['Norte','Centro','Sur']))
     tiempo.append(random.choice(['1 año','2 años','3 años']))
     costo.append(random.randint(100,500))
rtipo = ['telefonía','cable tv','internet']
rcantidad = [0.,0.,0.]
rtotal = [0.,0.,0.]
for i in range(len(nombre)):
         if tipo[i] == 'telefonía':
            rcantidad[0]= rcantidad[0]+1
            rtotal[0] = rtotal[0] + costo[i]
         elif tipo[i] == 'cable tv':
            rcantidad[1]= rcantidad[1]+1
            rtotal[1] = rtotal[1] + costo[i]
         elif tipo[i] == 'internet':
            rcantidad[2]= rcantidad[2]+1
            rtotal[2] = rtotal[2] + costo[i]     
def imprime_txt (texto, longitud):
        salida = '|'+ texto + ' ' * (longitud - len(texto))
        return salida
def imprime_mon(numero,longitud):
        snumero   = str('{:.2f}'.format(numero))
        salida = '|' + 'S/.' + ' ' * (longitud - len(snumero)-3) + snumero
        return salida
def imprime_num(numero,longitud):
        snumero   = str('{:.0f}'.format(numero))
        salida = '|' + ' ' * (longitud - len(snumero)) + snumero
        return salida

#definición de las opciones de menu
def mostrar_resultados():
    etiquetas2 = ['TIPO','CANTIDAD','TOTAL COSTO']
    letiquetas2 = [20,15,20]
    print('-'*(sum(letiquetas2)+len(etiquetas2)*2 +1))
    encabezado = ''
    for i in range(len(etiquetas2)):
        encabezado += ('| ' + etiquetas2[i]   + ' ' * (letiquetas2[i]   - len(etiquetas2[i]       )))
    print(encabezado[:-1],'|')  
    print('-'*(sum(letiquetas2)+len(etiquetas2)*2 +1))
    #columnas
    for i in range(3):
        print(imprime_txt(rtipo[i], letiquetas2[0]),
              imprime_num(rcantidad[i], letiquetas2[1]),
              imprime_mon(rtotal[i], letiquetas2[2]),
              '|')
    print('-'*(sum(letiquetas2)+len(etiquetas2)*2 +1))
    pass
def grabar_archivos():
    encuesta = pd.DataFrame(zip(nombre, tipo, zona, tiempo, costo), columns=['Nombre','Tipo de servicio','Zona','Tiempo de servicio','Costo'])
    encuesta.to_csv(r'C:/Users/david/Downloads/Casaño.csv')
    resultado = pd.DataFrame(zip(rtipo,rcantidad,rtotal), columns=['Tipo de servicio','Cantidad','Total Costo'])
    resultado.to_csv(r'C:/Users/david/Downloads/Suarez.csv')
    pass
def mostrar_reporte():
     #encabezado
    letiquetas = [20,20,15,25,18]
    print('-'*(sum(letiquetas)+len(etiquetas)*2 +1))
    encabezado = ''
    for i in range(len(etiquetas)):
        encabezado += ('| ' + etiquetas[i]   + ' ' * (letiquetas[i]   - len(etiquetas[i]       )))
    print(encabezado[:-1],'|')  
    print('-'*(sum(letiquetas)+len(etiquetas)*2 +1))
    

    #columnas
    for i in range(len(nombre)):
        print(imprime_txt(nombre[i], letiquetas[0]),
              imprime_txt(tipo[i], letiquetas[1]),
              imprime_txt(zona[i], letiquetas[2]),
              imprime_txt(tiempo[i], letiquetas[3]),
              imprime_mon(costo[i], letiquetas[4]),
              '|')
    print('-'*(sum(letiquetas)+len(etiquetas)*2 +1))
    pass
def salir():
    print('saliendo')
    pass
#definición del menú
def accion1():
    mostrar_reporte()
    pass
def accion2():
    mostrar_resultados()
    pass
def accion3():
    grabar_archivos()
    pass
def accion4():
    salir()
    pass

def menu():
    def imprime_menu():
            margen = ' '*60
            etiquetas3= ['    N°','              OPCIONES']
            letiquetas3 = [10,40]
            print(margen, '-'*(sum(letiquetas3)+len(etiquetas3)*2 +1))
            encabezado = ''
            for i in range(len(etiquetas3)):
                encabezado += ('| ' + etiquetas3[i]   + ' ' * (letiquetas3[i]   - len(etiquetas3[i]       )))
            print(margen, encabezado[:-1],'|')  
            print(margen, '-'*(sum(letiquetas3)+len(etiquetas3)*2 +1))
            
            numero = [1,2,3,4]
            opciones =['Mostrar encuesta','Mostrar resultado','Grabar archivos','Salida']
            #columnas
            for i in range(4):
                print(margen,
                      imprime_num(numero[i], letiquetas3[0]),
                      imprime_txt(opciones[i], letiquetas3[1]),
                      '|')
            print(margen, '-'*(sum(letiquetas3)+len(etiquetas3)*2 +1))


    margen = ' '*60
    opciones = {'1':('Mostrar encuesta', accion1),
                '2':('Mostrar resultado'         , accion2),
                '3':('Grabar archivos'        , accion3),
                '4':('Salida'  , accion4),
               }
    clave = None
    while clave != str(len(opciones.keys())):
        print(margen,'*********           MENÚ  DE  OPCIONES          *******')
        #for i in opciones:
            #print(i,')', opciones[i][0])
        imprime_menu()
        clave = input('Seleccione una opción: ')
        while clave not in opciones:
            print('Ingrese una opcion válida')
            clave = input('Seleccione una opciones')   
        opciones[clave][1]()
#PROGRAMA PRINCIPAL
menu()