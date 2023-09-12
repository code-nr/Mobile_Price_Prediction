# -*- coding: utf-8 -*-
"""StreamLit_app_MobilePrice.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fKbU6_xmex99WLFn9YYGAG5CNOGHSOS-
"""

import pickle5
import streamlit as st

# loading the trained model
pickle_in = open('XGBoost_model.pkl', 'rb')
regressor = pickle5.load(pickle_in)

@st.cache_data()
# defining the function which will make the prediction using the data which the user inputs
def prediction(Manufacturer, Category,Screen_Size, CPU,RAM, GPU, OS, Weight,  Touchscreen,IPS_Panel,Retina_display,Full_HD_display,Quad_HD_display,PPI,	SSD,	HDD,	Flash_Storage,	Hybrid_Storage):

  if Manufacturer == "Acer":
    MF_ID = 0
  elif Manufacturer == "Apple":
    MF_ID = 1
  elif Manufacturer == "Asus":
    MF_ID = 2
  elif Manufacturer == "Dell":
    MF_ID = 3
  elif Manufacturer == "HP":
    MF_ID = 4
  elif Manufacturer == "Lenovo":
    MF_ID = 10
  elif Manufacturer == "MSI":
    MF_ID = 11
  elif Manufacturer == "Toshiba":
    MF_ID = 16
  else:
    MF_ID =17
  if Category == "2 in 1 Convertible":
    Cat_Id = 0
  elif Category == "Gaming":
    Cat_Id = 1
  elif Category == "Notebook":
    Cat_Id = 2
  elif Category == "Ultrabook":
    Cat_Id = 3
  elif Category == "Workstation":
    Cat_Id = 4
  if CPU == "AMD A10-Serie":
    CPU_Id = 0
  elif CPU == "AMD A12-Series":
    CPU_Id = 1
  elif CPU == "Intel Core i3":
    CPU_Id = 9
  elif CPU == "Intel Core i5":
    CPU_Id = 10
  elif CPU == "Intel Core i7":
    CPU_Id = 11
  if OS == "Android":
    OS_Id = 0
  elif OS == "Chrome OS":
    OS_Id = 1
  elif OS == "Linux":
    OS_Id = 2
  elif OS == "Windows":
    OS_Id = 3
  elif OS == "macOS":
    OS_Id = 4
  if GPU == "AMD":
    GPU_ID = 0
  elif GPU == "ARM":
    GPU_ID = 1
  elif OS == "Intel":
    GPU_ID = 2
  elif GPU == "Nvidia":
    GPU_ID = 3
  if Touchscreen == "No":
    Touchscreen = 0
  else:
    Touchscreen = 1
  if IPS_Panel == "No":
    IPS_Panel = 0
  else:
    IPS_Panel = 1
  if Retina_display == "No":
    Retina_display = 0
  else:
    Retina_display = 1
  if Full_HD_display == "No":
    Full_HD_display = 0
  else:
    Full_HD_display = 1
  if Quad_HD_display == "No":
    Quad_HD_display = 0
  else:
    Quad_HD_display = 1
    # Making predictions
  prediction = regressor.predict(
        [[MF_ID, Cat_Id,Screen_Size, CPU_Id, RAM, GPU_ID, OS_Id, Weight, Touchscreen,IPS_Panel,Retina_display,Full_HD_display,Quad_HD_display,PPI,	SSD,	HDD,	Flash_Storage,	Hybrid_Storage]])
  return prediction
# this is the main function in which we define our webpage
def main():
    # front end elements of the web page
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;"> Pragyan AI Smart Phone Price Prediction ML App</h1>
    </div>
    """
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True)
    # following lines create boxes in which user can enter data required to make prediction
    Category = st.selectbox('Category',("2 in 1 Convertible","Gaming",'Notebook','Ultrabook', 'Workstation'))
    Manufacturer = st.selectbox('Manufacturer',("Dell","Lenovo",'HP','Asus', 'Acer','MSI', 'Toshiba','Apple'))
    CPU = st.selectbox('CPU',('AMD A10-Series', 'AMD A12-Series','Intel Core i3', 'Intel Core i5', 'Intel Core i7'))
    Screen_Size = st.number_input("Enter The Screen_Size value", min_value=10.0, max_value=20.0)
    RAM = st.number_input("Enter The RAM value", min_value=1.0, max_value=75.0)
    GPU =  st.selectbox('GPU',('AMD', 'ARM','Intel', 'Nvidia'))
    OS  =  st.selectbox('OS',('Android', 'Chrome OS','Linux', 'Windows', 'macOS' ))
    Weight = st.number_input("Enter Weight in Kg", min_value=0.0, max_value=20.0)
    Touchscreen  =  st.selectbox('Touchscreen',('Yes', 'No'))
    IPS_Panel  =  st.selectbox('IPS_Panel',('Yes', 'No'))
    Retina_display  =  st.selectbox('Retina_display',('Yes', 'No'))
    Full_HD_display  =  st.selectbox('Full_HD_display',('Yes', 'No'))
    Quad_HD_display  =  st.selectbox('Quad_HD_display',('Yes', 'No'))
    PPI = st.number_input("Enter PPI",min_value=0.0, max_value=600.0)
    SSD = st.number_input("Enter SSD value in GB",min_value=1, max_value=6000)
    HDD = st.number_input("Enter HDD value in GB",min_value=1, max_value=6000)
    Flash_Storage =  st.number_input("Enter Flash_Storage value in GB",min_value=1, max_value=6000)
    Hybrid_Storage =  st.number_input("Enter Hybrid_Storage value in GB",min_value=1, max_value=6000)
    result =""

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"):
        result = prediction(Manufacturer, Category,Screen_Size, CPU, RAM, GPU, OS, Weight, Touchscreen,IPS_Panel,Retina_display,Full_HD_display,Quad_HD_display,PPI,	SSD,	HDD,	Flash_Storage,	Hybrid_Storage)
        st.success('Your Smart Phone Sale Prediction is {}'.format(result))
        print(result)

if __name__=='__main__':
    main()