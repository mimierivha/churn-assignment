from flask import Flask, render_template, request
import pandas as pd



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        gender = request.form['gender']
        SeniorCitizen = request.form['SeniorCitizen']
        Partner = request.form['Partner']
        Dependents = request.form['Dependents']
        tenure = request.form['tenure']
        PhoneService = request.form['PhoneService']
        MultipleLines = request.form['MultipleLines']
        InternetService = request.form['InternetService']
        OnlineSecurity = request.form['OnlineSecurity']
        OnlineBackup = request.form['OnlineBackup']
        DeviceProtection = request.form['DeviceProtection']
        TechSupport = request.form['TechSupport']
        StreamingTV = request.form['StreamingTV']
        StreamingMovies = request.form['StreamingMovies']
        Contract = request.form['Contract']
        PaperlessBilling = request.form['PaperlessBilling']
        PaymentMethod = request.form['PaymentMethod']
        MonthlyCharges = request.form['MonthlyCharges']
        TotalCharges = request.form['TotalCharges']

        array1 = [gender, SeniorCitizen, Partner, Dependents, tenure, PhoneService, MultipleLines, InternetService,
                  OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract,
                  PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges]

        array1 = pd.to_numeric(array1)
        prediction = model.mp.predict([array1])
        print(prediction)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)