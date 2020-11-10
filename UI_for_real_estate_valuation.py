# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 18:20:39 2020

@author: User
"""

from tkinter import *
import pandas as pd
from sklearn import linear_model
data=pd.read_excel("D:\Datasets\Real estate valuation dataset\Real estate valuation data set.xlsx")
data=data.rename(columns={'No':'No','X1 transaction date':'Date', 'X2 house age':'Age',
       'X3 distance to the nearest MRT station':'Nearest_station',
       'X4 number of convenience stores':'Nearest_store', 'X5 latitude':'Lat', 'X6 longitude':'Long',
       'Y house price of unit area':'Price'})
X=data[['Age','Nearest_station','Nearest_store','Lat','Long']]
Y=data['Price']
print(X.max())
print(X.min())
regr=linear_model.LinearRegression()
regr.fit(X,Y)
print("Intercept: ",regr.intercept_)
print("\nCoefficients: ",regr.coef_)
window=Tk()
window.title("Real Estate valuation")
def regn(input_data):
    k=regr.predict([input_data])
    print(k)
    return k
def calc():
    age=float(txt1.get())
    station=float(txt2.get())
    stores=int(txt3.get())
    lat=float(txt4.get())
    lng=float(txt5.get())
    input_data=[age,station,stores,lat,lng]
    print(input_data)
    predicted_price=regn(input_data)
    lbl_result=Label(window,text="The price of the house will be %.2f units"%predicted_price[0])
    lbl_result.grid(row=1,column=2)
lbl0=Label(window,text="Enter the details below and see the price of house: ",width=50)
lbl0.grid(row=0,column=0)
lbl1=Label(window,text="Age of the house(0-43.8): ")
lbl1.grid(row=1,column=0)
txt1=Entry(window,width=10)
txt1.grid(row=1,column=1)
lbl2=Label(window,text="Distance from nearest railway station(23.4-6488.0): ")
lbl2.grid(row=2,column=0)
txt2=Entry(window,width=10)
txt2.grid(row=2,column=1)
lbl3=Label(window,text="Number of convenient stores nearby(0-10): ")
lbl3.grid(row=3,column=0)
txt3=Entry(window,width=10)
txt3.grid(row=3,column=1)
lbl4=Label(window,text="Latitude(24.93-25.01): ")
lbl4.grid(row=4,column=0)
txt4=Entry(window,width=10)
txt4.grid(row=4,column=1)
lbl5=Label(window,text="Longitude(121.47-121.56): ")
lbl5.grid(row=5,column=0)
txt5=Entry(window,width=10)
txt5.grid(row=5,column=1)
btn=Button(window,text="Calculate",command=calc)
btn.grid(row=6,column=1)
window.geometry('720x404')
window.mainloop()