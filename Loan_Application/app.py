import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle

app=Flask(__name__)
model=pickle.load(open('svm.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    try:
        features=[]
        features.append(int(request.form['Gender']))
        features.append(int(request.form['Married']))
        if int(request.form['Dependents']) == 0:
            features+=[0,0,0]
        elif int(request.form['Dependents']) == 1:
            features+=[1,0,0]
        elif int(request.form['Dependents']) == 2:
            features+=[0,1,0]
        elif int(request.form['Dependents']) == 3:
            features+=[0,0,1]
        features.append(int(request.form['Education']))
        features.append(int(request.form['Self_Employed']))
        features.append(int(request.form['Credit_History']))
        if int(request.form['Property_Area']) == 0:
            features+=[0,0]
        elif int(request.form['Property_Area']) == 1:
            features+=[1,0]
        elif int(request.form['Property_Area']) == 2:
            features+=[0,1]
        if int(request.form['Income']) == 0:
            features+=[0,0]
        elif int(request.form['Income']) == 1:
            features+=[1,0]
        elif int(request.form['Income']) == 2:
            features+=[0,1]

        final_feature=[np.array(features)]

        if model.predict(final_feature)==1:
            output= 'Your Loan Application Accepted'
        elif model.predict(final_feature)==0:
            output= 'Your Loan Application Rejected'
        return render_template('index.html',prediction_txt=output)
    except:
        return render_template('index.html',prediction_txt="Select All Values...")

if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host='0.0.0.0',port=8080)   # for AWS deployment