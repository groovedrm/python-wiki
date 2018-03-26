from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import AddressForm, WikiEntryForm
from app import db
from app.models import User, Entry

import requests
import pandas as pd

reports_url = 'http://api.staging.maprisk.com/reports'
geocode_url = 'http://api.staging.maprisk.com/geocode'
headers = {'x-auth-key': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI1YWI1NWNkOTY1MTA3MDAxYmM0ZmVhZmEiLCJleHAiOm51bGx9.LURAjucAQ269BzsxWcUp2PysqCZBNOam8oA39fjV-m4'}

@app.route('/')
@app.route('/index/')
def index():
	return render_template('index.html', title = 'Wiki - Home')

@app.route('/add/', methods = ['GET','POST'])
def add():
	form = WikiEntryForm()
	if form.validate_on_submit():
		if db.session.query(User.id).filter_by(username = form.entry_author.data).scalar() is not None:
			user_id = db.session.query(User.id).filter_by(username = form.entry_author.data)
			type = form.entry_type.data
			body = form.entry_body.data
			new_entry = Entry(type = type, body = body, user_id = user_id)

			db.session.add(new_entry)
			db.session.commit()

			flash("Entry submitted")
			return redirect(url_for('add'))

	return render_template('add.html', title = 'Wiki - Add Entry', form = form)

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
	
@app.route('/hazard/', methods = ['GET','POST'])
def hazard():
	form = AddressForm()
	if form.validate_on_submit():
		hazard_request = dict(reportList = 'floodRatingFEMA,floodRiskScore,slosh,stormSurge,propertyInformation,wildfireRiskScore', addressLine = form.address.data)
		resp = requests.request('GET', reports_url, headers = headers, params = hazard_request)
			
		flash('Hazard Requested For: {}'.format(form.address.data))
		flash(resp.text)
			
		return redirect(url_for('hazard'))
	
	return render_template('hazard.html', form = form)
		
		
	
	

#@app.route('/maprisk/')
#def maprisk():
#	query_string
#
#	return render_template('maprisk.html', data = MapRiskData)