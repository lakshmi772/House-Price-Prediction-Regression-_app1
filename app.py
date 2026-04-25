# create environment for  windowa
#py -m venv myenv
#activate the environment
#.\myenv\Scripts\Activate
#pip install streamlit scikit-learn pandas seaborn numpy
# create environment for  windowa
#py -m venv myenv
#activate the environment
#.\myenv\Scripts\Activate
#pip install streamlit scikit-learn pandas seaborn numpy

import pickle
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import StandardScaler


model=pickle.load(open('linear_model.pkl','rb'))

scaler=StandardScaler()

st.title('House Price Prediction (Regression)')




Square_Footage=st.number_input('Square_Footage',min_value=503,max_value=4999,value=1000) 

Num_Bedrooms=st.number_input('Num_Bedrooms',min_value=1,max_value=5,value=2)

Num_Bathrooms=st.number_input('Num_Bathrooms',min_value=1,max_value=3,value=2)

Year_Built=st.number_input('Year_Built',min_value=1950,max_value=2022,value=2000)

Lot_Size=st.number_input('Lot_Size',min_value=0.50,max_value=4.98,value=1.0)

Garage_Size=st.selectbox('Garage_Size',[0,1,2,3])

Neighborhood_Quality=st.number_input('Neighborhood_Quality',min_value=1,max_value=10,value=3)



#encoding for categorical column


input_features=pd.DataFrame({'Square_Footage':[Square_Footage], 'Num_Bedrooms':[Num_Bedrooms], 'Num_Bathrooms':[Num_Bathrooms], 'Year_Built':[Year_Built],
       'Lot_Size':[Lot_Size], 'Garage_Size':[Garage_Size], 'Neighborhood_Quality':[Neighborhood_Quality]})

input_features[['Square_Footage', 'Num_Bedrooms', 'Num_Bathrooms', 'Year_Built',
       'Lot_Size', 'Garage_Size', 'Neighborhood_Quality']]=scaler.fit_transform(input_features[['Square_Footage', 'Num_Bedrooms', 'Num_Bathrooms', 'Year_Built',
       'Lot_Size', 'Garage_Size', 'Neighborhood_Quality']])

if st.button('Predict'): 
    prediction = model.predict(input_features)[0]
    st.success(f'Predicted House Price: {prediction:.2f}')
  
