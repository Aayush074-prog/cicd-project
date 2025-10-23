# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Aayush here from Panel F1 27!, Hello from my AWS SERVER! It's deployed!"

def add(a, b):
    return a + b

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)