from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

with open("titanic_model.pkl", 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=["GET","POST"])
def home():
    prediction = None
    if request.method == "POST":
        pclass = int(request.form['pclass'])
        sex = int(request.form['sex'])
        age = float(request.form['age'])
        sibsp = int(request.form['sibsp'])
        parch = int(request.form['parch'])
        fare = float(request.form['fare'])
        embarked = int(request.form['embarked'])

        features = np.array([[pclass, sex, age, sibsp, parch, fare, embarked]])
        prediction = model.predict(features)[0]

    return render_template("index.html", prediction = prediction)

if __name__ == '__main__':
    app.run(debug=True)