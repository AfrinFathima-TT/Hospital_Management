import streamlit as st
from Patient_Views import PatientManager
patient_instance = PatientManager()

tab1 , tab2 = st.tabs(["Add","view"])
with tab1:
    st.title("Add new patient")
    Name = st.text_input("Enter your name")
    Age = st.text_input("Enter your age")
    Gender = st.selectbox("Select your gender",["Male","Female","Others"])
    Mobile = st.text_input("Enter your mobile number")
    Disease = st.text_input("Enter your disease")
    Doctor = st.text_input("Enter doctor name")
    Admission_date = st.date_input("Enter admission_date (yyyy/mm/dd)")
    if st.button("Add new patient"):
        patient_instance.post(Name =Name, Age =Age,Gender= Gender,Mobile = Mobile, Disease =Disease,Doctor = Doctor,Admmission_date = Admission_date)
        st.success("New patient details added successfully...!")
with tab2:
    st.title("View patient details")
    records = patient_instance.get()
    if records :
        st.table(records)
    else:
        st.warning("No Patient found...!")

