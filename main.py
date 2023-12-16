from flask import Flask, request, render_template
import pandas as pandas
import pickle

app = Flask(__name__)

with open ('modelfix.pkl','rb') as file:
    model = pickle.load(file)

@app.route('/')
def first ():
    return render_template('home.html')

@app.route('/Carupat.AI')
    