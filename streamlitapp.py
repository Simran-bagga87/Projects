import streamlit as sl
import pickle 
import numpy as np
def loaddata():
    with open('data','rb') as file:
        data = pickle.load(file)
        return data

data = loaddata()


def myproject():

    no_of_customer = sl.text_input("Enter the No of Customer",0)
    menuprice = sl.text_input("Enter the Menu Price",0)
    Marketing_Spend = sl.text_input("Enter the Marketing Spend",0)
    Cuisine_Type = sl.selectbox('Select the Cuisine Type', ['Japanese', 'Italian', 'American', 'Mexican'])
    Average_Customer_Spending = sl.text_input("Enter the Average Customer Spending",0)
    promotion = sl.radio('Promotions', [0, 1])
    Review = sl.slider('Enter Review', min_value=1, max_value=50, value=5)
    
 
    no_of_customer=float(no_of_customer)
    menuprice=float(menuprice)
    Marketing_Spend=float(Marketing_Spend)
    Average_Customer_Spending=float(Average_Customer_Spending)
    promotion=float(promotion)
    Review=float(Review)
    x=np.array([[no_of_customer,menuprice,Marketing_Spend,Cuisine_Type,Average_Customer_Spending,promotion,Review]])
    encode = data['encoding']
    model = data['model']
    x[:,3] = encode.transform(x[:,3])
        
    x = x.astype(float)
    print(x)
    ok = sl.button('calculate')
    if ok:
        value = model.predict(x)
        sl.write("the monthly income is $",round(float(value),2))



myproject()

    
 