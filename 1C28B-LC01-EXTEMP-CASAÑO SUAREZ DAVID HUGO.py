#Inicio
vendedor = ['Torres', 'Zavala', 'Mejía', 'Cerna',]
zona = ['Norte', 'Sur', 'Norte', 'Oeste'] 
producto = ['Naranjas', 'Pimientos', 'Pepinos', 'Limones']
ventask =  [600.0, 1200.0, 320.0, 945.0]
ventasm =  [1800.0, 3000.0, 384.0, 5670.0]
desc1 = [0,0,0,0]
desc2 =[0,0,0,0]
bonif1 =[0,0,0,0]
bonif2 = [0,0,0,0]
bonif3 = [0,0,0,0]
obs = ['','','','']


etiquetas = ['VENDEDOR','ZONA','PRODUCTO','VENTAS EN KG','VENTAS SOLES', 'DESC1', 'DESC2','BONIF1','BONIF2','BONIF3','OBSERVACIÓN']


letiquetas = [12,6,12,15,15,12,12,12,12,12,18]
lvendedor = 12
lzona = 6
lproducto = 12 
lventask = 12
lventasm = 14
ldesc1= 12
ldesc2= 12
lbonif1 = 12
lbonif2 = 12
lbonif3 = 12
lobs = 18
encabezado = ''
#PROCESO
print('-'*183)
for i in range(len(etiquetas)):
  encabezado += ('| ' + etiquetas[i]   + ' ' * (letiquetas[i]   - len(etiquetas[i]       )+2))
print(encabezado[:-1],'|')  
print('-'*183)

for i in range(len(vendedor)):
  if ventask[i]<= 600 :     desc1[i] = 0.04*ventasm[i]
  else:                     desc1[i] = 0.015*ventasm[i]
  if zona[i] == 'Sur':      desc2[i] = 0.03*ventasm[i]
  else:                     desc2[i] = 0.015*ventasm[i]
  if ventasm[i]> 1500 :     bonif1[i] = ventasm[i]/8
  else:                     bonif1[i] = ventasm[i]/6
  if ventask[i]> 1000 :     bonif2[i] = 0.07*ventasm[i]
  else:                     bonif2[i] = 0.035*ventasm[i]
  if zona[i] == 'Norte':    bonif3[i] = 0.08*ventasm[i]
  else:                     bonif3[i] = 0.04*ventasm[i]
  if ventasm[i]> 2000 :     obs[i] = 'Promovido'
  else:                     obs[i] = 'No promovido'
  
  #para variables tipo numérico
  sventask   = str('{:.2f}'.format(ventasm[i]))
  sventasm   = str('{:.0f}'.format(ventask[i]))
  sdesc1     = str('{:.2f}'.format(desc1[i]))
  sdesc2     = str('{:.2f}'.format(desc2[i]))
  sbonif1    = str('{:.2f}'.format(bonif1[i]))
  sbonif2    = str('{:.2f}'.format(bonif2[i]))
  sbonif3    = str('{:.2f}'.format(bonif3[i]))
  #SALIDA
  print('|',                                           vendedor[i]   ,' ' * (lvendedor   -   len(vendedor[i]       )),
        '|',                                           zona[i]    ,' ' * (lzona    - len(zona[i]        )),
        '|',                                           producto[i]  ,' ' * (lproducto  - len(producto[i]      )),
        '|', ' ' * (lventasm   - len(sventasm       )+1), sventasm     ,
        '|','S/.',' ' * (lventask   - len(sventask       )-1), sventask     ,
        '|','S/.',' ' * (ldesc1     - len(sdesc1         )-4), sdesc1       ,
        '|','S/.',' ' * (ldesc2     - len(sdesc2         )-4), sdesc2       ,
        '|','S/.',' ' * (lbonif1   - len(sbonif1         )-4), sbonif1      ,
        '|','S/.',' ' * (lbonif2   - len(sbonif2         )-4), sbonif2      ,
        '|','S/.',' ' * (lbonif3   - len(sbonif3         )-4), sbonif3      ,
        '|',                                           obs[i]  ,' ' * (lobs  - len(obs[i]      )),                             
        '|')

print('-'*183)

###ff