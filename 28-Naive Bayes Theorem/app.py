import pickle
import pandas as pd
from flask import Flask, request, render_template


app = Flask(__name__)


# Load model and columns
model = pickle.load(
    open("model/gaussian_nb.pkl", "rb")
)


columns = pickle.load(
    open("model/columns.pkl", "rb")
)



@app.route("/")
def index():
    return render_template("home.html")



@app.route("/predictdata", methods=["POST"])
def predict_datapoint():

    try:

        # User Input

        total_bill = float(request.form["total_bill"])

        tip = float(request.form["tip"])

        sex = request.form["sex"].title()

        smoker = request.form["smoker"].title()

        day = request.form["day"].title()

        size = int(request.form["size"])



        # Create DataFrame

        new_data = pd.DataFrame({

            "total_bill":[total_bill],

            "tip":[tip],

            "sex":[sex],

            "smoker":[smoker],

            "day":[day],

            "size":[size]

        })



        # One Hot Encoding

        new_data = pd.get_dummies(

            new_data,

            columns=[
                "sex",
                "smoker",
                "day"
            ],

            drop_first=True,

            dtype=int

        )



        # Match training columns

        new_data = new_data.reindex(

            columns=columns,

            fill_value=0

        )



        # Prediction

        prediction = model.predict(new_data)


        probability = model.predict_proba(new_data)



        confidence = round(
            probability.max()*100,
            2
        )



        return render_template(

            "home.html",

            results=prediction[0],

            confidence=confidence

        )



    except Exception as e:


        return render_template(

            "home.html",

            error=e

        )




if __name__=="__main__":

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )