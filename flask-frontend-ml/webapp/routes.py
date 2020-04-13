from flask import request,jsonify,render_template,redirect
from flask import url_for,session
import pickle
import numpy as np
from webapp import app
from webapp.forms import ValueForm
import json

model = pickle.load(open('webapp/models/model.pkl','rb'))

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html',title='Home',form = ValueForm())


@app.route('/result',methods=['GET', 'POST'])
def result():
	data = json.loads(session['data'])
	# form = request.args['form']
	# form = json.loads(session['form'])
	return render_template('result.html',title = 'result',data=data)



@app.route('/login',methods=['GET', 'POST'])
def login():
	form = ValueForm()
	if form.validate_on_submit():
		value = form.value.data
		prediction = model.predict([[np.array(value)]])
		session['data'] = json.dumps(prediction[0])
		# session['form'] = json.dumps(form)
		return redirect(url_for('result',form = form))
	return render_template('form.html',title = 'login',form=form)

@app.route('/jsform',methods=['GET', 'POST'])
def jsform():
	return render_template('jsform.html',title = 'jsform')


@app.route('/predict')
def predict():
	try:
		data = request.args.get('proglang', 0, type=float)
		prediction = model.predict([[np.array(data)]])
		output = round(prediction[0])
		return jsonify(result=("Salary: " + str(output)))
	except Exception as e:
		return str(e)