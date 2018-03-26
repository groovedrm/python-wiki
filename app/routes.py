from app import app
from flask import rrender_template, flash, redirect, url_for
from app.forms import AddressForm

import requests
import pandas as pd

geocode_url = 'http://api.staging.maprisk.com/geocode'
headers = {'x-auth-key': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI1YWI1NWNkOTY1MTA3MDAxYmM0ZmVhZmEiLCJleHAiOm51bGx9.LURAjucAQ269BzsxWcUp2PysqCZBNOam8oA39fjV-m4'}

@app.route('/')
@app.route('/index/')
def index():
	return render_template('index.html', title = 'Wiki - Home')

@app.route('/add/')
def add():
	return render_template('add.html', title = 'Wiki - Add Entry')

@app.route('/display/')
def display():
	dataTable = pd.read_csv('re_deals.csv', delimiter = ',', index_col = None)
	dataDisplay = dataTable.to_html()
	return render_template('display.html', data = dataDisplay)
	# Mostly working correctly, now just need to understand how to loop through
	# so that the HTML is actually rendered with display.html, rather than 
	# displayed in HTML markup form.

	# Older test render:
	# return render_template('display.html', title = 'Wiki - All Entries')

@app.route('/geocode/', methods = ['GET','POST'])
def geocode():
	form = AddressForm()
	if form.validate_on_submit():
		geocode_string = {'addressLine': form.address.data}
		geocode_response = requests.request('GET', geocode_url, headers = headers, params = geocode_string)
		
		flash('Geocode Requested For: {} and geocode string {}'.format(form.address.data, geocode_string))
		flash(geocode_response.text)

		return redirect(url_for('geocode'))
	return render_template('geocode.html', form = form)

#@app.route('/maprisk/')
#def maprisk():
#	query_string
#
#	return render_template('maprisk.html', data = MapRiskData)