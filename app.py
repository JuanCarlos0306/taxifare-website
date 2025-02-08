import streamlit as st
from datetime import datetime
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

st.header("Ingrese la fecha y hora de la solicitud")
fecha = st.date_input("Fecha")
hora = st.time_input("Hora")
fecha_hora = datetime.combine(fecha, hora)

st.header("Ingrese las coordenadas de recogida")
pickup_longitude = st.number_input("Longitud de recogida")
pickup_latitude = st.number_input("Latitud de recogida")

st.header("Ingrese las coordenadas de entrega")
dropoff_longitude = st.number_input("Longitud de entrega")
dropoff_latitude = st.number_input("Latitud de entrega")

st.header("Ingrese la cantidad de pasajeros")
passenger_count = st.number_input("Cantidad de pasajeros", min_value=1)


url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')


#2. Let's build a dictionary containing the parameters for our API...
dicc = {
    "pickup_datetime": fecha_hora,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}

#3. Let's call our API using the `requests` package...
req = requests.get("https://taxifare.lewagon.ai/predict", params=dicc)

#4. Let's retrieve the prediction from the **JSON** returned by the API...
if req.status_code == 200:
    # Obtener el resultado de la predicción
    resultado = req.json()["fare"]
    st.write(f"El costo estimado del viaje es: ${resultado:.2f}")
## Finally, we can display the prediction to the user
