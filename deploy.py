from flask import Flask, render_template,request
import pickle

app = Flask(__name__)
model = pickle.load(open('saved_model.sav','rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html', **locals())

@app.route('/predict',methods=['POST','GET'])
def predict():
    SepalLengthCm = float(request.form['SepalLengthCm'])
    SepalWidthCm = float(request.form['SepalWidthCm'])
    PatelLengthCm = float(request.form['PatelLengthCm'])
    PatelWidthCm = float(request.form['PatelWidthCm'])
    result = model.predict([[ SepalLengthCm,SepalWidthCm,PatelLengthCm,PatelWidthCm]])[0]
    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)