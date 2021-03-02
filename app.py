# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('rent_vs_buy_d_tree_model.pkl', 'rb'))


@app.route('/')
def show_predict():
    return render_template('predictorform.html')
@app.route('/results', methods = ['POST'])
def results():
    if request.method == 'POST':
        cost = int(request.form['cost'])
        fuel = request.form['fuel']
        km = int(request.form['km'])
        if (fuel == 'Petrol'):
            X = np.array([[0, 0, 1, cost, km]])
        elif(fuel == 'Diesel'):
            X = np.array([[1, 0, 0, cost, km]])
        else:
            X = np.array([[0, 1, 0, cost, km]])
        res = model.predict(X)
        if (res == 1):
            res = "Based on the information given, renting a car will be a better alternative."
        else:
            res = "Based on the information given, buying a car will be a better alternative."
        return render_template('resultsform.html', result = res)

if __name__=="__main__":
    app.run(debug=true)
