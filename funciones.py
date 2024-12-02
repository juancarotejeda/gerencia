def check_parada(cur,parada):
    cur.execute(f"SELECT balance_banco FROM tabla_index WHERE nombre = '{parada}' ")
    check=cur.fetchall()
    for valor in check:
        if valor[0] > 1000.00:
            return True
        else: 
            return False
        
def check_funcion(cur,funcion):
    codg=[]
    func=[]
    cur.execute(f"SELECT codigo,funcion FROM administracion WHERE funcion = '{funcion}' ")
    check=cur.fetchall()
    if check !=[]:
      for valor in check:
        codg=valor[0]
        func=valor[1]
      return codg,func
    
    else: 
        return False        
        
        
        
        
    
def listado_paradas(cur):
    nombre=[]
    cur.execute("SELECT nombre FROM tabla_index")  
    db_paradas=cur.fetchall()
    for nomb in db_paradas:
        nombre+=nomb     
    return nombre

def listado_paradas_norte(cur):
    nombre=[]
    cur.execute("SELECT nombre FROM tabla_index WHERE zona='Norte'")  
    db_paradas=cur.fetchall()
    for nomb in db_paradas:
        nombre+=nomb     
    return nombre


def listado_paradas_sur(cur):
    nombre=[]
    cur.execute("SELECT nombre FROM tabla_index WHERE zona='Sur'")  
    db_paradas=cur.fetchall()
    for nomb in db_paradas:
        nombre+=nomb     
    return nombre

def listado_paradas_este(cur):
    nombre=[]
    cur.execute("SELECT nombre FROM tabla_index WHERE zona='Este'")  
    db_paradas=cur.fetchall()
    for nomb in db_paradas:
        nombre+=nomb     
    return nombre

def listado_paradas_distrito(cur):
    nombre=[]
    cur.execute("SELECT nombre FROM tabla_index WHERE zona='Distrito Nacional'")  
    db_paradas=cur.fetchall()
    for nomb in db_paradas:
        nombre+=nomb     
    return nombre

def listado_paradas_sdn(cur):
    nombre=[]
    cur.execute("SELECT nombre FROM tabla_index WHERE zona='Sdn'")  
    db_paradas=cur.fetchall()
    for nomb in db_paradas:
        nombre+=nomb     
    return nombre

def listado_paradas_sde(cur):
    nombre=[]
    cur.execute("SELECT nombre FROM tabla_index WHERE zona='Sde'")  
    db_paradas=cur.fetchall()
    for nomb in db_paradas:
        nombre+=nomb     
    return nombre

def listado_paradas_sdo(cur):
    nombre=[]
    cur.execute("SELECT nombre FROM tabla_index WHERE zona='Sdo'")  
    db_paradas=cur.fetchall()
    for nomb in db_paradas:
        nombre+=nomb     
    return nombre



def listado_administrativo(cur):
    cur.execute("SELECT funcion FROM administracion")  
    db_paradas=cur.fetchall()     
    return db_paradas

def info_parada(cur,parada):
    if parada !=[]:
      cur.execute(f"SELECT codigo,nombre,direccion,municipio,provincia,zona,cuota,pago,banco,num_cuenta FROM  tabla_index  WHERE nombre='{parada}'" )
      infos=cur.fetchall()     
      return infos
    else:
      return [] 

def info_cabecera(cur,parada):
    if parada !=[]:          
        cur.execute(f'SELECT nombre FROM {parada}')
        seleccion=cur.fetchall()
        cant=len(seleccion)  
        presidente = []       
        cur.execute(f"SELECT nombre FROM {parada}  WHERE funcion = 'Presidente'")   
        press=cur.fetchone()
        if press != None:  
            for pres in press:   
                presidente=pres
        else:     
            presidente='No disponible'   
        veedor = []
        cur.execute(f"SELECT nombre FROM {parada}  WHERE funcion = 'Veedor'")   
        presd=cur.fetchone()
        if presd != None:
          for prex in presd:
            veedor=prex 
        else:
            veedor='No disponible'           
        return cant,presidente,veedor 
    else:
        return 0,'No disponible','No disponible'
               
     
def lista_miembros(cur,parada):
    if parada !=[]: 
      listas=[]
      cur.execute(f"SELECT id,nombre,cedula,telefono,funcion  FROM {parada}")
      miembros=cur.fetchall()
      for miembro in miembros:     
         listas+=miembro    
      lista=dividir_lista(listas,5)    
      return lista
    else:
      return []  
    
def diario_general(cur,parada):
    if parada !=[]: 
        prestamos=[]
        ingresos=[]
        gastos=[]
        aporte=[]
        pendiente=[]
        abonos=[]
        balance_bancario=[]
        cur.execute(f"SELECT  prestamos, ingresos, gastos, aporte, pendiente, abonos, balance_banco FROM tabla_index WHERE nombre='{parada}' " )  
        consult=cur.fetchall()
        for valor in consult:
            prestamos=valor[0]
            ingresos=valor[1]
            gastos=valor[2]
            aporte=valor[3]
            pendiente=valor[4]
            abonos=valor[5]
            balance_bancario=valor[6]
        balance=(aporte + ingresos + abonos )-(gastos+prestamos)
        data=(balance,prestamos,ingresos,gastos,aporte,pendiente,abonos,balance_bancario)   
        return data
    else:
        return 0,0,0,0,0,0,0,0

def prestamo_aport(cur,parada):
    cur.execute(f"SHOW TABLES LIKE '{parada}_cuota'")
    vericar=cur.fetchall()
    if vericar !=[]:
      vgral=[]
      cur.execute(f"SELECT nombre FROM {parada}")
      list_nomb=cur.fetchall()
      for nombre in list_nomb:
         cur.execute(f"SELECT COUNT(estado) FROM {parada}_cuota WHERE estado = 'pago' and nombre='{nombre[0]}'") 
         var_x = cur.fetchall()
         for var_p in var_x:
              var1=var_p[0]
         cur.execute(f"SELECT COUNT(estado) FROM {parada}_cuota WHERE estado = 'no_pago' and nombre='{nombre[0]}'")
         var_z = cur.fetchall()
         for var_n in var_z:
              var2=var_n[0]   
         sub_t=var1+var2
         if sub_t != 0 :    
          avg=round((var1/sub_t)*100,2)
         else:
          avg = 0.00               
         vgral+=(nombre[0],var1,var2,sub_t,avg) 
      list_1=dividir_lista(vgral,5)                    
      return list_1
    else:
      return [] 




def dividir_lista(lista,lon) : 
    return [lista[n:n+lon] for n in range(0,len(lista),lon)]     


def aportacion(cur,parada):           
    cur.execute(f"SELECT codigo, nombre, cedula, telefono, funcion FROM {parada}")
    data=cur.fetchall()
    return data
  
def verif_p(cur,parada,cedula,password):
    cur.execute(f"SELECT * FROM tabla_index WHERE  adm_password = '{password}'")
    result=cur.fetchall()
    if result:
      cur.execute(f"SELECT * FROM {parada} WHERE  cedula = '{cedula}'")                                       
      accounts =cur.fetchall()
      if accounts != []:
         return True
      else:
         return False 
    else: 
        return False

def nombres_miembro(cur,parada):
        listado=[]
        cur.execute(f"SELECT nombre FROM {parada} ")
        nombres=cur.fetchall()
        for nombre in nombres:
            listado += nombre
        return listado 


def dat_miembros(cur,parada,miembro):
    cur.execute(f"SELECT nombre,cedula,telefono,funcion FROM {parada} WHERE nombre='{miembro}'")
    listado=cur.fetchall()
    return listado

