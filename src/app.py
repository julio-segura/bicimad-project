import streamlit as st
import pandas as pd
import numpy as np
from pickle import load

# Load your pre-trained model
# Replace 'your_model.pkl' with the path to your model file
with open(r'..\models\bicimad_model.sav', 'rb') as f:
    model = load(f)

def predict_bike_count(data):
    # Use your model to make predictions
    # This function should be modified according to how your model expects input
    prediction = model.predict(data)
    return prediction

def main():
    st.title("Bike Rental Prediction App")

    # Creating inputs for the user to enter data
    
    fleet = st.number_input('Fleet', min_value=1, max_value = 2)
    trip_minutes = st.number_input('Trip Duration in Minutes', min_value=0, max_value = 60)
    
    hour = st.slider('Hour of the Day', 0, 23)
   

    # Button to make prediction
    if st.button('Predict Bike Count'):
        # Creating a dataframe from the inputs
        data = pd.DataFrame([[fleet, trip_minutes, hour]],
                            columns=['fleet', 'trip_minutes', 'hour'])
        
        # Get the prediction
        prediction = predict_bike_count(data)

        # Display the prediction
        st.success(f'The predicted bike count is {prediction[0]}')

if __name__ == '__main__':
    main()
