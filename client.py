import sys
import json
import requests

def service_client():
	conv = {'text': 'Hola soy Nelsi'}
	s = json.dumps(conv)
	res = requests.post("http://0.0.0.0:5000/spam/", json=s)
	#print(res)
	
service_client()