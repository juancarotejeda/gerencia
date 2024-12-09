import mysql.connector,funciones,os
from mysql.connector import errorcode
from flask import Flask, render_template,flash, request,  redirect, url_for
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.secret_key=os.getenv("APP_KEY")
DB_HOST =os.getenv('DB_HOST')
DB_USERNAME =os.getenv("DB_USERNAME")
DB_PASSWORD =os.getenv("DB_PASSWORD")
DB_NAME =os.getenv("DB_NAME")


connection =mysql.connector.connect(
    host=DB_HOST,
    user=DB_USERNAME,
    password=DB_PASSWORD,
    database=DB_NAME,
    autocommit=True
)

@app.route("/")
def login():   
    cur = connection.cursor() 
    resultado=funciones.listado_administrativo(cur)
    funcion=[]
    for funcionarios in resultado:
       funcion += funcionarios  
    cur.close()                   
    return render_template('login.html',funcion=funcion)

@app.route("/verificacion", methods=["GUET","POST"])
def verificacion(): 
   msg = ''
   if request.method == 'POST':        
    funcion = request.form['funcion']
    codigo_personal = request.form['codigo_personal'] 
    cur = connection.cursor()   
    estacion=funciones.check_funcion(cur,funcion)
   if estacion != False:           
    if codigo_personal == estacion[0] and funcion == estacion[1] : 
      if codigo_personal == 'ge00': 
            paradas=funciones.listado_paradas(cur)
            parada=[]       
            fecha = datetime.strftime(datetime.now(),"%Y %m %d - %H")
            informacion=funciones.info_parada(cur,parada)
            cabecera=funciones.info_cabecera(cur,parada) 
            miembros=funciones.lista_miembros(cur,parada)                
            diario=funciones.diario_general(cur,parada) 
            cuotas_hist=funciones.prestamo_aport(cur,parada)
            cur.close()
            return render_template('index.html',paradas=paradas,informacion=informacion,cabecera=cabecera,fecha=fecha,miembros=miembros,diario=diario,cuotas_hist=cuotas_hist)                  
        
      elif codigo_personal == 'grn00':
            cur = connection.cursor() 
            paradas=funciones.listado_paradas_norte(cur)
            parada=[]  
            fecha = datetime.strftime(datetime.now(),"%Y %m %d - %H")
            informacion=funciones.info_parada(cur,parada)
            cabecera=funciones.info_cabecera(cur,parada) 
            miembros=funciones.lista_miembros(cur,parada)                
            diario=funciones.diario_general(cur,parada) 
            cuotas_hist=funciones.prestamo_aport(cur,parada)
            cur.close()
            return render_template('index_norte.html',paradas=paradas,informacion=informacion,cabecera=cabecera,fecha=fecha,miembros=miembros,diario=diario,cuotas_hist=cuotas_hist)      

      elif codigo_personal == 'grs00':
            cur = connection.cursor() 
            paradas=funciones.listado_paradas_sur(cur)
            parada=[]  
            fecha = datetime.strftime(datetime.now(),"%Y %m %d - %H")
            informacion=funciones.info_parada(cur,parada)
            cabecera=funciones.info_cabecera(cur,parada) 
            miembros=funciones.lista_miembros(cur,parada)                
            diario=funciones.diario_general(cur,parada) 
            cuotas_hist=funciones.prestamo_aport(cur,parada)
            cur.close()
            return render_template('index_sur.html',paradas=paradas,informacion=informacion,cabecera=cabecera,fecha=fecha,miembros=miembros,diario=diario,cuotas_hist=cuotas_hist)      

      elif codigo_personal == 'gre00':
            cur = connection.cursor() 
            paradas=funciones.listado_paradas_este(cur)
            parada=[]  
            fecha = datetime.strftime(datetime.now(),"%Y %m %d - %H")
            informacion=funciones.info_parada(cur,parada)
            cabecera=funciones.info_cabecera(cur,parada) 
            miembros=funciones.lista_miembros(cur,parada)                
            diario=funciones.diario_general(cur,parada) 
            cuotas_hist=funciones.prestamo_aport(cur,parada)
            cur.close()
            return render_template('index_este.html',paradas=paradas,informacion=informacion,cabecera=cabecera,fecha=fecha,miembros=miembros,diario=diario,cuotas_hist=cuotas_hist)      
 
      elif codigo_personal == 'gdn00':
            cur = connection.cursor() 
            paradas=funciones.listado_paradas_distrito(cur)
            parada=[]  
            fecha = datetime.strftime(datetime.now(),"%Y %m %d - %H")
            informacion=funciones.info_parada(cur,parada)
            cabecera=funciones.info_cabecera(cur,parada) 
            miembros=funciones.lista_miembros(cur,parada)                
            diario=funciones.diario_general(cur,parada) 
            cuotas_hist=funciones.prestamo_aport(cur,parada)
            cur.close()
            return render_template('index_distrito.html',paradas=paradas,informacion=informacion,cabecera=cabecera,fecha=fecha,miembros=miembros,diario=diario,cuotas_hist=cuotas_hist)      
  
      elif codigo_personal == 'gsn00':
            cur = connection.cursor() 
            paradas=funciones.listado_paradas_sdn(cur)
            parada=[]  
            fecha = datetime.strftime(datetime.now(),"%Y %m %d - %H")
            informacion=funciones.info_parada(cur,parada)
            cabecera=funciones.info_cabecera(cur,parada) 
            miembros=funciones.lista_miembros(cur,parada)                
            diario=funciones.diario_general(cur,parada) 
            cuotas_hist=funciones.prestamo_aport(cur,parada)
            cur.close()
            return render_template('index_sdn.html',paradas=paradas,informacion=informacion,cabecera=cabecera,fecha=fecha,miembros=miembros,diario=diario,cuotas_hist=cuotas_hist)      
   
      elif codigo_personal == 'gse00':
            cur = connection.cursor() 
            paradas=funciones.listado_paradas_sde(cur)
            parada=[]  
            fecha = datetime.strftime(datetime.now(),"%Y %m %d - %H")
            informacion=funciones.info_parada(cur,parada)
            cabecera=funciones.info_cabecera(cur,parada) 
            miembros=funciones.lista_miembros(cur,parada)                
            diario=funciones.diario_general(cur,parada) 
            cuotas_hist=funciones.prestamo_aport(cur,parada)
            cur.close()
            return render_template('index_sde.html',paradas=paradas,informacion=informacion,cabecera=cabecera,fecha=fecha,miembros=miembros,diario=diario,cuotas_hist=cuotas_hist)      
    
      elif codigo_personal == '00':
            return render_template('galeria_motoben.html')  
        
      elif codigo_personal == '01':
            return render_template('guia.html')             

      elif codigo_personal == 'gso00':
            cur = connection.cursor() 
            paradas=funciones.listado_paradas_sdo(cur)
            parada=[]  
            fecha = datetime.strftime(datetime.now(),"%Y %m %d - %H")
            informacion=funciones.info_parada(cur,parada)
            cabecera=funciones.info_cabecera(cur,parada) 
            miembros=funciones.lista_miembros(cur,parada)                
            diario=funciones.diario_general(cur,parada) 
            cuotas_hist=funciones.prestamo_aport(cur,parada)
            cur.close()
            return render_template('index_sdo.html',paradas=paradas,informacion=informacion,cabecera=cabecera,fecha=fecha,miembros=miembros,diario=diario,cuotas_hist=cuotas_hist)  
     
    else:
        msg = 'Sin acceso a estas paginas!'          
        flash(msg)           
        return redirect(url_for('login')) 
       
@app.route("/indice", methods=["GUET","POST"])
def indice():
    if request.method == 'POST':        
        parada = request.form['parada'] 
        cur = connection.cursor()          
        fecha = datetime.strftime(datetime.now(),"%Y %m %d - %H")
        informacion=funciones.info_parada(cur,parada) 
        cabecera=funciones.info_cabecera(cur,parada) 
        miembros=funciones.lista_miembros(cur,parada)                
        diario=funciones.diario_general(cur,parada) 
        cuotas_hist=funciones.prestamo_aport(cur,parada)
        paradas=funciones.listado_paradas_norte(cur)
        cur.close()
        return render_template('index.html',paradas=paradas,informacion=informacion,cabecera=cabecera,fecha=fecha,miembros=miembros,diario=diario,cuotas_hist=cuotas_hist)     

@app.route("/indice_norte", methods=["GUET","POST"])
def indice_norte():
    if request.method == 'POST':        
        parada = request.form['parada'] 
        cur = connection.cursor()          
        fecha = datetime.strftime(datetime.now(),"%Y %m %d - %H")
        informacion=funciones.info_parada(cur,parada) 
        cabecera=funciones.info_cabecera(cur,parada) 
        miembros=funciones.lista_miembros(cur,parada)                
        diario=funciones.diario_general(cur,parada) 
        cuotas_hist=funciones.prestamo_aport(cur,parada)
        paradas=funciones.listado_paradas_norte(cur)
        cur.close()
        return render_template('index_norte.html',paradas=paradas,informacion=informacion,cabecera=cabecera,fecha=fecha,miembros=miembros,diario=diario,cuotas_hist=cuotas_hist)     

@app.route("/indice_sur", methods=["GUET","POST"])
def indice_sur():
    if request.method == 'POST':        
        parada = request.form['parada'] 
        cur = connection.cursor()          
        fecha = datetime.strftime(datetime.now(),"%Y %m %d - %H")
        informacion=funciones.info_parada(cur,parada) 
        cabecera=funciones.info_cabecera(cur,parada) 
        miembros=funciones.lista_miembros(cur,parada)                
        diario=funciones.diario_general(cur,parada) 
        cuotas_hist=funciones.prestamo_aport(cur,parada)
        paradas=funciones.listado_paradas_sur(cur)
        cur.close()
        return render_template('index_sur.html',paradas=paradas,informacion=informacion,cabecera=cabecera,fecha=fecha,miembros=miembros,diario=diario,cuotas_hist=cuotas_hist)     

@app.route("/indice_este", methods=["GUET","POST"])
def indice_este():
    if request.method == 'POST':        
        parada = request.form['parada'] 
        cur = connection.cursor()          
        fecha = datetime.strftime(datetime.now(),"%Y %m %d - %H")
        informacion=funciones.info_parada(cur,parada) 
        cabecera=funciones.info_cabecera(cur,parada) 
        miembros=funciones.lista_miembros(cur,parada)                
        diario=funciones.diario_general(cur,parada) 
        cuotas_hist=funciones.prestamo_aport(cur,parada)
        paradas=funciones.listado_paradas_este(cur)
        cur.close()
        return render_template('index_este.html',paradas=paradas,informacion=informacion,cabecera=cabecera,fecha=fecha,miembros=miembros,diario=diario,cuotas_hist=cuotas_hist)     

@app.route("/indice_sdn", methods=["GUET","POST"])
def indice_sdn():
    if request.method == 'POST':        
        parada = request.form['parada'] 
        cur = connection.cursor()          
        fecha = datetime.strftime(datetime.now(),"%Y %m %d - %H")
        informacion=funciones.info_parada(cur,parada) 
        cabecera=funciones.info_cabecera(cur,parada) 
        miembros=funciones.lista_miembros(cur,parada)                
        diario=funciones.diario_general(cur,parada) 
        cuotas_hist=funciones.prestamo_aport(cur,parada)
        paradas=funciones.listado_paradas_sdn(cur)
        cur.close()
        return render_template('index_sdn.html',paradas=paradas,informacion=informacion,cabecera=cabecera,fecha=fecha,miembros=miembros,diario=diario,cuotas_hist=cuotas_hist)     

@app.route("/indice_sde", methods=["GUET","POST"])
def indice_sde():
    if request.method == 'POST':        
        parada = request.form['parada'] 
        cur = connection.cursor()          
        fecha = datetime.strftime(datetime.now(),"%Y %m %d - %H")
        informacion=funciones.info_parada(cur,parada) 
        cabecera=funciones.info_cabecera(cur,parada) 
        miembros=funciones.lista_miembros(cur,parada)                
        diario=funciones.diario_general(cur,parada) 
        cuotas_hist=funciones.prestamo_aport(cur,parada)
        paradas=funciones.listado_paradas_sde(cur)
        cur.close()
        return render_template('index_sde.html',paradas=paradas,informacion=informacion,cabecera=cabecera,fecha=fecha,miembros=miembros,diario=diario,cuotas_hist=cuotas_hist)     

@app.route("/indice_sdo", methods=["GUET","POST"])
def indice_sdo():
    if request.method == 'POST':        
        parada = request.form['parada'] 
        cur = connection.cursor()          
        fecha = datetime.strftime(datetime.now(),"%Y %m %d - %H")
        informacion=funciones.info_parada(cur,parada) 
        cabecera=funciones.info_cabecera(cur,parada) 
        miembros=funciones.lista_miembros(cur,parada)                
        diario=funciones.diario_general(cur,parada) 
        cuotas_hist=funciones.prestamo_aport(cur,parada)
        paradas=funciones.listado_paradas_sdo(cur)
        cur.close()
        return render_template('index_sdo.html',paradas=paradas,informacion=informacion,cabecera=cabecera,fecha=fecha,miembros=miembros,diario=diario,cuotas_hist=cuotas_hist)     

@app.route("/indice_distrito", methods=["GUET","POST"])
def indice_distrito():
    if request.method == 'POST':        
        parada = request.form['parada'] 
        cur = connection.cursor()          
        fecha = datetime.strftime(datetime.now(),"%Y %m %d - %H")
        informacion=funciones.info_parada(cur,parada) 
        cabecera=funciones.info_cabecera(cur,parada) 
        miembros=funciones.lista_miembros(cur,parada)                
        diario=funciones.diario_general(cur,parada) 
        cuotas_hist=funciones.prestamo_aport(cur,parada)
        paradas=funciones.listado_paradas_distrito(cur)
        cur.close()
        return render_template('index_distrito.html',paradas=paradas,informacion=informacion,cabecera=cabecera,fecha=fecha,miembros=miembros,diario=diario,cuotas_hist=cuotas_hist)     

@app.route("/guia")
def guia():
    return render_template('guia.html')

@app.route("/galeria")
def galeria():
    return render_template('galeria_motoben.html')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
