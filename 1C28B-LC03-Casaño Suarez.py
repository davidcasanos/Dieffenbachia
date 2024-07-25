#INCIO
lista1_casano=['Aroste, Adrian','Cutte, David','Paredes, Jamila','Salazar, David','Davalos, Naldina','Alarcon, Dulce','Ruiz, Yasin','Camayo, Jhonatan','Condori, Alonso','Gonzales, Arlene']
dni=['991049651','992159852','990746416','998810505','993254088','991582467','992257876','997490372','991930764','998491514']
dserv =[9,4,5,3,7,9,5,6,7,6]
precio = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]
igv = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]
total = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]
cobro = 0.

def accion1():
    print('                                                 CUADRO DE INGRESOS           ','\n')
    print('-----------------------------------------------------------------------------------------------------------------------------')
    print('     CLIENTE               DNI                     DÍAS SERVICIO         PRECIO              IGV                    TOTAL')
    print('-----------------------------------------------------------------------------------------------------------------------------')
    ldserv = 18
    llista1_casano = 18
    lprecio = 15
    ldni = 18
    ligv    = 18
    ltotal  = 15
    global cobro 
    for i in range(len(lista1_casano)):
        precio[i] = 55*dserv[i]
        igv[i] = 0.18*55*dserv[i]
        total[i] = 1.18*55*dserv[i]
        cobro = cobro + total[i]
        sdserv   = str('{:,.0f}'.format(dserv[i]))
        sprecio  = str('{:,.2f}'.format(precio[i]))
        sigv     = str('{:,.2f}'.format(igv[i]))
        stotal   = str('{:,.2f}'.format(total[i]))
    
        print('|',lista1_casano[i],' ' *       (llista1_casano   - len(lista1_casano[i]  )),
              '|',dni[i],' ' *       (ldni   - len(dni[i]  )),
        '|',' ' * (ldserv   - len(sdserv         )-3), sdserv     ,
        '|',' ' * (lprecio  - len(sprecio         )-3),'S/', sprecio    ,
        '|',' ' * (ligv  - len(sigv        )-3),'S/', sigv    ,
        '|',' ' * (ltotal   - len(stotal         )-3),'S/  ', stotal    ,

        '|')
    #SALIDA    
    scobro = str('{:,.2f}'.format(cobro))    
    print('-----------------------------------------------------------------------------------------------------------------------------')
    print('                                                                                                     COBRO TOTAL S/', scobro )
    print('-----------------------------------------------------------------------------------------------------------------------------')
def accion2():
    print('\n', 'INGRESE EL REGISTRO A AGREGAR: ')
    xcliente = input('cliente')
    xdni = input ('DNI')
    xdserv = int(input('DIAS SERVICIO'))
    lista1_casano.append(xcliente)
    dni.append(xdni)
    dserv.append(xdserv)
    precio.append(55*xdserv)
    igv.append(0.18*55*xdserv)
    total.append(1.18*55*xdserv)

#PROCESO
def accion3():
    print('\n', 'INGRESE EL DNI A ELIMINAR: ')
    x = str(input(' dni '))
    for i in range (len(dni)-1):
        if x == dni[i]:
            del lista1_casano[i]
            del dni[i]
            del dserv[i]
            del precio[i]
            del igv[i]
            del total[i]
    
def accion4():
    print('\n', 'INGRESE EL DNI A MODIFICAR: ')
    x = str(input(' dni '))
    for i in range (len(dni)-1):
        if x == dni[i]:
            lista1_casano[i]= input(' INGRESE EL NOMBRE DE CLIENTE ')
            dni[i] = input(' INGRESE EL DNI ')
            dserv[i] = int(input(' INGRESE LOS DÍAS DE SERVICIO '))
            precio[i] = 55*dserv[i]
            igv[i] = 0.18*55*dserv[i]
            total[i] = 1.18*55*dserv[i]

def accion5():
    print('Conclusiones:')
    print('- Las funciones ayudan a definir cada una de las opciones del menú.','\n' )
    print('- La búsqueda se efectúa con la sentencia for.','\n' )
    print('- Para el cobro fue necesario utizar una variable global.','\n' )
    print('- Para los datos de entrada se fuerza a entero o a string según se necesite.','\n' )
def accion6():
    print('Saliendo')
def menu():
    opciones = {'1':('Mostrar reportes'                , accion1),
                '2':('Agregar'              , accion2),
                '3':('Eliminar'     , accion3),
                '4':('Modificar dato' , accion4),
                '5':('Conclusiones'          , accion5),
                '6':('Salida'                 , accion6),
               }
    clave = None
    while clave != '6':
        print('***  MENÚ  DE  OPCIONES  ***')
        for i in opciones:
            print(i,')', opciones[i][0])
        clave = input('Seleccione una opción: ')
        while clave not in opciones:
            print('Ingrese una opcion válida')
            clave = input('Seleccione una opciones')
           
        opciones[clave][1]()
        

#PROGRAMA PRINCIPAL
menu()
  