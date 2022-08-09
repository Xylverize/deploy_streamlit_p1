
from flask import Flask, jsonify, request
import pickle
import pandas as pd

#init
app = Flask(__name__)

#open model
def open_model(model_path):
    """
    helper function for loading model
    """
    with open(model_path, "rb") as model_file:
        model = pickle.load(model_file)

    return model

model_forest = open_model("model_forest_tuning.pkl")

def car_price_inference(data, model=model_forest):
    """
    input : list with length 16 --> 'Price', 'Levy', 'Manufacturer', 'Model', 'Prod. year',
       'Category', 'Leather interior', 'Fuel type', 'Engine volume', 'Mileage',
       'Cylinders', 'Gear box type', 'Drive wheels', 'Doors', 'Wheel', 'Color',
       'Airbags'
    output : predicted class : (idx)
    """
 
    columns = ['Levy', 'Manufacturer', 'Model', 'Prod. year',
       'Category', 'Leather interior', 'Fuel type', 'Engine volume', 'Mileage',
       'Cylinders', 'Gear box type', 'Drive wheels', 'Doors', 'Wheel', 'Color',
       'Airbags']
    data = pd.DataFrame([data], columns=columns)
    res = model.predict(data)
    return res


@app.route("/test")
def test():
    return "<h1>Halo dari flask!</h1>"

@app.route("/about")
def about():
    return "Ini Halaman about"

@app.route("/")
def car_price_predict():
    args = request.args
    levy            = args.get("Levy", type=int, default=-0.47222411)
    manufacturer    = args.get("Manufacturer", type=str, default=0.6528929)
    model           = args.get("Model", type=str, default=-0.67582873)
    prod            = args.get("Prod. year", type=int, default=-1.13105596)
    category        = args.get("Category", type=str, default=-0.46852129)
    leather         = args.get("Leather interior", type=str, default= -0.77777778)
    fuel            = args.get("Fuel type", type=str, default=3)
    engine          = args.get("Engine volume", type=float, default=2)
    mileage         = args.get("Mileage", type=int, default=2)
    cylinders       = args.get("Cylinders", type=float, default=1)
    gearbox         = args.get("Gear box type", type=int, default=0)
    drive           = args.get("Drive wheels", type=str, default=0)
    doors           = args.get("Doors", type=str, default=1)
    wheel           = args.get("Wheel", type=str, default=0)
    color           = args.get("Color", type=str, default=0)
    airbags         = args.get("Airbags", type=int, default=4)
    new_data        = [levy,manufacturer,model,prod,category,leather,fuel,engine,
                        mileage,cylinders,gearbox,drive,doors,wheel,color,airbags]

    price = car_price_inference(new_data)
    response = jsonify(result=str(price))
    return response


# test kode di local
# jika ingin deploy komenkan code dibawah
# app.run(debug=True)