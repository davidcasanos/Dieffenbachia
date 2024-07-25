descripcion = ['Torno KZ99', 'Fresadora AV67', 'Taladro WE34', 'Estabilizador WR45', 'Equipo XYZ']
peso = [380.0, 360.0, 140.0, 110.0, 235.0]
pais = ['Usa', 'Japón', 'Francia', 'Inglaterra', 'Usa']
precioe =[10856.0, 23456.0, 32623.0, 28698.0, 10569.0]
precio = []
flete =[]
comision =[]
total = []



for i in range(len(descripcion)):
    if pais [i] == 'Usa':
       vtc = 3.15
       vflete = 9.0
    if pais [i] == 'Japón':
       vtc = 1.166
       vflete = 8.0
    if pais [i] == 'Francia':
       vtc = 3.87
       vflete = 7.0
    if pais [i] == 'Inglaterra':
       vtc = 4.762
       vflete = 2.0 
    precio.append(precioe[i]*vtc)
    if precio[i] < 20000.0 : vp = 0
    if precio[i] >= 20000.0 and precio[i] < 25000.0 : vp = 0.14
    if precio[i] >= 25000.0 and precio[i] < 35000.0 : vp = 0.12
    if precio[i] >= 35000.0 : vp = 0.10
    
    flete.append(peso[i]*vflete)
    comision.append(precio[i]*vp)
    total.append(precio[i]+ flete[i]+ comision[i])



a = '|  Descripción        |  Peso Kg.  |     Pais    |      Precio     |  precio S/. | Flete S/. |   Comisión S/.   |   Total S/.   |'

print('┌','-' * (len(a)-4),'┐')
print(a)
print('├','-' * (len(a)-4),'┤')

ldescripcion   = 18 
lpeso    = 10
lpais  = 10
lprecioe = 16
lprecio   = 13
lflete = 8
lcomision = 15
ltotal = 12

#columnas
for i in range(len(descripcion)):
  speso   = str('{:.2f}'.format(peso[i]))
  sprecioe   = str('{:,.2f}'.format(precioe[i]))
  sprecio   = str('{:,.2f}'.format(precio[i]))
  sflete   = str('{:,.2f}'.format(flete[i]))
  scomision   = str('{:,.2f}'.format(comision[i]))
  stotal = str('{:,.2f}'.format(total[i]))
  print('|',descripcion[i],' ' * (ldescripcion   - len(descripcion[i]       )),
        '|',peso[i]    ,' ' * (lpeso   - len(speso)),
        '|',pais[i]  ,' ' * (lpais  - len(pais[i])),
        '|',precioe[i] ,' ' * (lprecioe- len(sprecioe)),
        
        '|',' ' * (lprecio   - len(sprecio         )-3), sprecio     ,
        '|',' ' * (lflete - len(sflete)), sflete ,
        '|',' ' * (lcomision - len(scomision       )), scomision   ,
        '|',' ' * (ltotal - len(stotal       )), stotal   ,
        '|')
print('└',
        '-----------------------------------------------------------------------------------------------------------------------------' ,'┘')

print('Conclusiones')

print('El flete hacia Japón es similar al de USA')
print('Los precios de los países europeos son más elevados que el resto')
print('Cuando un producto tiene más peso, su flete es mayor')
print('Las comisiones tienen valores proporcionales al precio')