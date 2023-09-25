import pandas as pd
import numpy as np
import streamlit as st
import joblib 
import warnings
warnings.filterwarnings('ignore')


model = joblib.load('package.pkl')
data = pd.read_csv('Telco-Customer-Churn.csv')
    
def model_prediction(gender,Partner, Dependents,PhoneService, MultipleLines, InternetService,OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport,StreamingTV, StreamingMovies, Contract, PaperlessBilling,PaymentMethod,SeniorCitizen,tenure,MonthlyCharges,TotalCharges):
    new = [gender,Partner, Dependents,PhoneService, MultipleLines, InternetService,OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport,StreamingTV, StreamingMovies, Contract, PaperlessBilling,PaymentMethod, SeniorCitizen,tenure,MonthlyCharges,TotalCharges]
    new = pd.DataFrame([new],columns = ['gender','Partner', 'Dependents','PhoneService', 'MultipleLines', 'InternetService','OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport','StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling','PaymentMethod', 'SeniorCitizen','tenure','MonthlyCharges','TotalCharges'])
    prediction = model.predict(new)
    return prediction

def screen_function():
    st.title("Telecom - Telstra")
    
    screen_look = """
    <div style = 'background-color:orange;'>
    <h2 style = 'color:white;text-align:centre;'>Customer Churn Prediction</h2>
    </div>
    """
    st.markdown(screen_look,unsafe_allow_html = True)
    
    gender= st.selectbox("Gender",np.unique(data['gender']))
    Partner= st.selectbox("Partner",np.unique(data['Partner']))
    Dependents= st.selectbox("Dependents",np.unique(data['Dependents']))
    PhoneService= st.selectbox("PhoneService",np.unique(data['PhoneService']))
    MultipleLines= st.selectbox("MultipleLines",np.unique(data['MultipleLines']))
    InternetService= st.selectbox("InternetService",np.unique(data['InternetService']))
    OnlineSecurity= st.selectbox("OnlineSecurity",np.unique(data['OnlineSecurity']))
    OnlineBackup= st.selectbox("OnlineBackup",np.unique(data['OnlineBackup']))
    DeviceProtection= st.selectbox("DeviceProtection",np.unique(data['DeviceProtection']))
    TechSupport= st.selectbox("TechSupport",np.unique(data['TechSupport']))
    StreamingTV= st.selectbox("StreamingTV",np.unique(data['StreamingTV']))
    StreamingMovies= st.selectbox("StreamingMovies",np.unique(data['StreamingMovies']))
    Contract= st.selectbox("Contract",np.unique(data['Contract']))
    PaperlessBilling= st.selectbox("PaperlessBilling",np.unique(data['PaperlessBilling']))
    PaymentMethod= st.selectbox("PaymentMethod",np.unique(data['PaymentMethod']))
    SeniorCitizen = st.selectbox("SeniorCitizen",[0,1])
    tenure = st.number_input("Enter your Tenure",min_value = 1)
    MonthlyCharges =  st.number_input("Enter your Monthly Charges",min_value = 1)
    TotalCharges = st.number_input("Enter your Total Charges",min_value = 1)
                       
    result = ""
    if st.button("Find Churn Prediction"):
        result = model_prediction(gender,Partner, Dependents,PhoneService, MultipleLines, InternetService,OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport,StreamingTV, StreamingMovies, Contract, PaperlessBilling,PaymentMethod, SeniorCitizen,tenure,MonthlyCharges,TotalCharges)
        
    if (result == "No"):
        st.success("Customer might not opt for churning")
    elif (result == "Yes"):
        st.success("Potential Churning Customer")    
        
if __name__ == '__main__':
    screen_function()