import streamlit as st
import requests

st.title("Aplikasi Prediksi Harga Mobil")

levy            = st.number_input("Levy",value=1399)
manufacturer    = st.text_input("Manufacturer",value='LEXUS')
model           = st.text_input("Model",value='RX 450')
prod            = st.number_input("Prod. year",value=2010)
category        = st.text_input("Category",value='Jeep')
leather         = st.text_input("Leather interior",value='Yes')
fuel            = st.text_input("Fuel Type",value='Hybrid') 
engine          = st.number_input("Engine volume",value=3.5)
mileage         = st.number_input("Mileage",value=186005) 
cylinders       = st.number_input("Cylinders",value=6.0) 
gearbox         = st.text_input("Gear box",value='Automatic')
drivewheels     = st.text_input("Drivewheels",value='4x4')
doors           = st.text_input("Doors",value='04-05')
wheel           = st.text_input("Wheel",value='Left wheel')
color           = st.text_input("Color",value='Silver')
airbags         = st.number_input("Airbags",value=12) 



# inference
URL = "http://127.0.0.1:5000/car_price"
param = {"Levy"           : levy,
        "Manufacturer"    : manufacturer,
        "Model"           : model,
        "Prod. year"      : prod,
        "Category"        : category,
        "Leather interior": leather,
        "Fuel Type"       : fuel,
        "Engine volume"   : engine,
        "Mileage"         : mileage,
        "Cylinders"       : cylinders,
        "Gearbox"         : gearbox,
        "Drivewheels"     : drivewheels,
        "Doors"           : doors,
        "Wheel"           : wheel,
        "Color"           : color,
        "Airbags"         : airbags,
        }


r = requests.get(URL, json=param)
res = r.json()

if r.status_code == 200:
    res = r.json()
    st.title(res)
else:
    st.title("Unexpected Error")

