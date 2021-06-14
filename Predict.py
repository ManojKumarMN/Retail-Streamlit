# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 16:37:21 2021

@author: manoj
"""

import numpy as np
import pandas as pd
import pickle
import streamlit as st

#from PIL import Image

page_bg_img = '''
<style>
label {
    display: inline-block;
    font-weight: bold;
    font-size: 16px;
}
button {
    display: inline-flex;
    -webkit-box-align: center;
    align-items: center;
    -webkit-box-pack: center;
    justify-content: center;
    font-weight: 400;
    padding: 0.25rem 0.75rem;
    border-radius: 0.25rem;
    margin: 0px;
    line-height: 1.6;
    width: auto;
    background-color: tomato !important;
    border: 1px solid tomato !important;
    color: white !important;
}
button:hover {
    display: inline-flex;
    -webkit-box-align: center;
    align-items: center;
    -webkit-box-pack: center;
    justify-content: center;
    font-weight: 400;
    padding: 0.25rem 0.75rem;
    border-radius: 0.25rem;
    margin: 0px;
    line-height: 1.6;
    width: auto;
    background-color: tomato;
    border: 1px solid tomato;
    color: white !important;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)



#pickle = open("Linear_Model.pkl","rb")
#Linear = pickle.load(pickle)
#print(Linear)

Retail = pd.read_csv(r'C:\Users\manoj\Desktop\Model Deployment\Prediction.csv')

def welcome():
    return "Welcome All"

def predict_customer_next_purcahse(CustomerID):
    
    df = pd.DataFrame(Retail)
    df1 = df[df['CustomerID'].astype(str) == CustomerID]   
       
    if len(df1) == 1:
        for i in df1['NextPurchaseDayRange'].values:
            if i == 1:
                return 'Yes, Customer is going to shop in 30days'
            return 'No, Customer is not going to shop in next 30 days'
    return 'Enter valid Customer ID'

def main():
    
    st.markdown("<div style='text-align: center;'><img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTv5_DATuZauo8P-EzqgXKiCERHHjwOS3CShA&usqp=CAU' style='text-align: center;' alt='Girl in a jacket' width='200' height='200'></div>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color:tomato;'>Retail Store Prediction</h1>", unsafe_allow_html=True)
    html_temp = """
    <div style="padding:10px">
    <h2 style="text-align:center;color:blue;">Predicting Customer's Next Purcahse</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    #Input features
    
    CustomerID = st.text_input(label="CustomerID")

    #st.sidebar.header('RFM SCORE')
    #Recency = st.sidebar.slider(
     #  'Recency',
     #   0, 3, (0, 1)
     #   )
    #Frequency = st.sidebar.slider(
    #    'Frequency',
     #   0, 3,(0, 1)
    #    )
   # Revenue = st.sidebar.slider(
     #   'Revenue',
     #   0, 3, (0, 1)
     #   )

    result=""
    if st.button("Predict"):
        #prediction = Linear.predict([['CustomerID']])
        result = predict_customer_next_purcahse(CustomerID)
        if result:
            st.success('{}'.format(result))

if __name__=='__main__':
    main()

