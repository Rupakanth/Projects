from flask import Flask, request, render_template
from joblib import load
import pandas as pd

model = load('BigMart_modl.joblib')

columns = ['Item_Weight', 'Item_Fat_Content', 'Item_Visibility', 'Item_Type',
       'Item_MRP', 'Outlet_Establishment_Year', 'Outlet_Location_Type',
       'Outlet_Type', 'Outlet_Size']


app = Flask('app')

@app.route('/',methods = ['GET','POST'])
def hello_world():
	if request.method == 'POST':
		try:
			ItemWeight = float(request.form['Item_Weight'])
			FatContent = int(request.form['Item_Fat_Content'])
			ItemVisibility = float(request.form['Item_Visibility'])
			ItemType = str(request.form['Item_Type'])
			ItemMRP = float(request.form['Item_MRP'])
			OutletEstablishmentYear = int(request.form['Outlet_Establishment_Year'])
			LocationType = str(request.form['Outlet_Location_Type'])
			OutletType = str(request.form['Outlet_Type'])
			OutletSize = str(request.form['Outlet_Size'])

			result = model.predict(pd.DataFrame([[ItemWeight,FatContent,ItemVisibility,ItemType,ItemMRP,OutletEstablishmentYear,LocationType,OutletType,OutletSize]],columns = columns))
			return render_template('index.html',predictedvalue = round(result[0],2))
		except:
			result = 'Incorrect input'
			return render_template('index.html',predictedvalue=result)

	return render_template('index.html')

@app.route('/report',methods=['GET','POST'])
def get_report():
	return render_template('your_report.html')

app.run(host='localhost',port=8080,debug=True)




