from flask import Flask, request,jsonify
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load( open('model.pkl','rb'))
print(model.predict([[1.8]]))

@app.route('/')
@app.route('/home')
def home():
	return 'home'

@app.route('/api',methods=['POST'])
def api():
	data = request.get_json(force=True)
	prediction = model.predict([[np.array(data['value'])]])
	output = prediction[0]
	return jsonify(output)

if __name__ == '__main__':
	app.run(port = 5000, debug=True)