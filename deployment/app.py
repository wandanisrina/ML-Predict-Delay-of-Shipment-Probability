import streamlit as st
import eda
import model

page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploration Data Analysis', 'Model Prediksi'])

if page == 'Home Page':
    st.header('Machine Learning Model : Predict Delay of Shipment Probability') 
    st.write('by Wanda Nisrina Aqilah')
    st.write('**BACKGROUND**')
    st.caption('The logistics sector is an important sector that contributes to ensuring the supply chain will run smoothly, especially in industries that depend on delivery such as retail, manufacturing, and healthcare. ' \
        'In practice, operational problems are still often encountered that indirectly affect the delivery process, therefore it is necessary to analyze what factors contribute to delivery time. ' \
        'By conducting this analysis, the parties involved are expected to gain insight into minimizing factors that contribute to delays so as to increase business efficiency.')
    st.write(' ')
    st.write('**DATASET OVERVIEW**')
    st.caption('The dataset provides a comprehensive collection of logistics operations data from WN Logistics from 2021-2024. ' \
        'In this dataset, it contains 26 columns and 32.065 rows. All columns are explained factors that contribute in delay of shipment that will be analysis.')
    st.write(' ')
    st.write('**PROBLEM STATEMENT**')
    st.caption('Delays in delivery can certainly be a problem because it can reduce customer satisfaction. ' \
        'Therefore, it is important to predict what factors affect delivery time. ' \
        'Hopefully, by creating this machine learning model, company can take corrective and preventive action to reduce delay in delivery so that it can improve logistics efficiency.')
    st.write(' ')
    st.write('**CONCLUSION**')
    st.caption('The model used is "Boosting with GradientBoostingRegressor after Hyperparameter Tunning". ' \
        'The error of model is 25-30% and it perform **underfit**. This indicates that the model its not perform well and tend to underpredict. ' )
    st.write(' ')
    st.write('**RECOMMENDATION**')
    st.caption('In order to perform well, the model have to be improved. One of the way to improve it by doing features creation. ' \
        'Moreover, conduct training and evaluation of the model until a low error of <10-15% is obtained so that it can provide relevant and accurate results. ' )

elif page == 'Exploration Data Analysis':
    eda.run()
else:
     model .run()