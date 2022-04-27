from flask import Flask,render_template, request, Response, redirect, url_for
app = Flask(__name__)
import csv
import io
import pandas as pd
import geopandas as gpd
import contextily
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#Dichiarazioni dei geodataframe
dati = []

quartieri=gpd.read_file('/workspace/EasyMilano/static/file/ds964_nil_wm-20220405T093028Z-001.zip')
mezzi_superficie=gpd.read_file('/workspace/EasyMilano/static/file/tpl_percorsi.geojson')
uffici_postali=pd.read_csv('/workspace/EasyMilano/static/file/uffici_postali_milano.csv')
civici=pd.read_csv('/workspace/EasyMilano/static/file/civici.csv')
comandi_polizialocale=gpd.read_file('/workspace/EasyMilano/static/file/geocoded_comandi-decentrati-polizia-locale__final.geojson')
scuole=pd.read_csv('/workspace/EasyMilano/static/file/CITTA_METROPOLITANA_MILANO_-_Scuole_di_ogni_ordine_e_grado.csv')
metro=gpd.read_file('/workspace/EasyMilano/static/file/tpl_metropercorsi.geojson')
stradario=pd.read_csv('/workspace/EasyMilano/static/file/stradario (2).csv')

#home e registrazione

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return  render_template('register.html')
    else: 
        name = request.form.get('name')
        surname = request.form.get('surname')
        via = request.form.get('via')
        pwd = request.form.get('pwd')
        cpwd = request.form.get('cpwd')



    
        
        if name != '' and pwd != '' and surname != '' and pwd == cpwd and via != '':
            new_dati = {'name':name, 'pwd':pwd, 'surname':surname , 'via' : via}
            dati = dati.append(new_dati,ignore_index=True)
            return redirect(url_for(''))
        else:
            return f'errore {username,pwd,cpwd,sex}'



#verifico se posso scrivere



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)