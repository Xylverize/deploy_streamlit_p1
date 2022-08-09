
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
    levy            = args.get("Levy", type=int, default=655)
    manufacturer    = args.get("Manufacturer", type=str, default="HYUNDAI")
    model           = args.get("Model", type=str, default='Elantra')
    prod            = args.get("Prod. year", type=int, default=2015)
    category        = args.get("Category", type=str, default='Sedan')
    leather         = args.get("Leather interior", type=str, default='Yes')
    fuel            = args.get("Fuel type", type=str, default='Diesel')
    engine          = args.get("Engine volume", type=float, default=1.6)
    mileage         = args.get("Mileage", type=int, default=52313)
    cylinders       = args.get("Cylinders", type=float, default=4.0)
    gearbox         = args.get("Gear box type", type=int, default='Automatic')
    drive           = args.get("Drive wheels", type=str, default='Front')
    doors           = args.get("Doors", type=str, default='4-5')
    wheel           = args.get("Wheel", type=str, default='Left wheel')
    color           = args.get("Color", type=str, default='White')
    airbags         = args.get("Airbags", type=int, default=4)
    new_data        = [levy,manufacturer,model,prod,category,leather,fuel,engine,
                        mileage,cylinders,gearbox,drive,doors,wheel,color,airbags]

    price = car_price_inference(new_data)
    response = jsonify(result=str(price))
    return response


# test kode di local
# jika ingin deploy komenkan code dibawah
# app.run(debug=True)