from flask import Flask
from threading import Thread
import random

app = Flask('')

@app.route('/')
def home():
	return "Hello"

def run():
  port = random.randint(1024, 8080)
  app.run(host='0.0.0.0', port=port)

def keep_alive():
	t = Thread(target=run)
	t.start()