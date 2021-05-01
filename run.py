from flask import Flask, jsonify, request
import test
import Insurance_db

app=Flask(__name__)

@app.route('/register', methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        data = request.form
        response = Insurance_db.registeration(data)
    return jsonify({'msg':response})

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        data = request.form
        response1 = Insurance_db.login(data)
    return jsonify({'msg': response1})

@app.route('/predict_charges', methods = ['GET','POST'])
def prediction():
    data=request.form
    if request.method =='POST':
        age= int(data['age'])
        bmi= float(data['bmi'])
        children= int(data['children'])
        smoker= data.get('smoker')
        prediction= test.predict_charges(age, bmi, children, smoker)
        Insurance_db.save_predictions(age, bmi, children, smoker, prediction)

        return "The Predicted charges is Rs. {} ".format(prediction)

if __name__ == "__main__":
    print("Starting Python Flask Server For Insurance Charges Prediction...")
    app.run(host='0.0.0.0',port='5002')