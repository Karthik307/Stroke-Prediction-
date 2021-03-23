from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import pandas as pd
import sklearn
import joblib
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = joblib.load('stroke.pkl')  
  
# Use the loaded model to make predictions 

@ app.route('/', methods = ['GET'])
def Home():
    return render_template('Homepage.html')


standard_to = StandardScaler()

@ app.route("/predict", methods = ['POST'])
def predict():
    if request.method == 'POST':
        #Gender
        Gender = request.form['gender']
        if Gender == 'Male':
            Gender = 1
        if Gender == 'Female':
            Gender = 0
        else:
            Gender=2
         #Age   
        Age = int(request.form['age'])
        #Hypertension
        Hypertension = request.form['hypertension']
        if Hypertension == 'Yes':
            Hypertension = 1
        else:
            Hypertension = 0
        #Heart condition
        Heart = request.form['heart_disease']
        if Heart == 'Yes':
            Heart = 1
        else:
            Heart = 0
        #Marriage
        Married = request.form['ever_married']
        if Married == 'Married':
            Married = 1
        else:
            Married = 0
        #Work enviornment
        work=request.form['work_type']
        if work=='Govt_job':
            work=0
        if work=='Never_worked':
            work=1
        if work=='Private':
            work=2
        if work=='Self-employed':
            work=3
        if work=='children':
            work=4
        #Redidence area
        Residence=request.form['Residence_Area']
        if Residence=='Urban':
            Residence=0
        if Residence=='Rural':
            Residence=1
        #Glucose
        avg_glucose_level=int(request.form['avg_glucose_level'])
        #Body mass index
        bmi=int(request.form['bmi'])
        #Smoking habbits
        smoking_status=request.form['smoking_status']
        if smoking_status=='Unkonown':
            smoking_status=0
        if smoking_status=='formerly smoked':
            smoking_status=1
        if smoking_status=='never smoked':
            smoking_status=2
        if smoking_status=='smokes':
            smoking_status=3
        #stroke prediction
        stroke = model.predict([[Gender, Age, Hypertension, Heart, Married, work, Residence,avg_glucose_level, bmi,smoking_status]])
        if stroke<0:
            return render_template('Homepage.html',prediction_text="Sorry Invalid Data")
        if stroke==0:
            return render_template('Homepage.html',prediction_text="You are safe from stroke {}!".format(stroke))
        if stroke==1:
            return render_template('Homepage.html',prediction_text="Consult a doctor {}!".format(stroke))
            
    else:
        return render_template('Homepage.html')
    

if __name__ == "__main__":
    app.run(debug = True)