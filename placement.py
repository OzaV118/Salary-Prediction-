import numpy as np
import pickle
import streamlit as st


salary_model = pickle.load(open("Model\salary_model.sav", "rb"))

gender_map = {"Male": 1, "Female": 0}
board_map = {"Central": 1, "Others": 0}
workexp_map = {"Yes": 1, "No": 0}
specialization_map = {"Mkt&HR": 0, "Mkt&Fin": 1}
hsc_subject_map = {"Commerce": 0, "Science": 1, "Arts": 2}
degree_type_map = {"Sci&Tech": 0, "Comm&Mgmt": 1, "Others": 2}

st.set_page_config(page_title="Salary Prediction", layout="centered")
st.title("Salary Prediction for Placed Students")

col1, col2 = st.columns(2)
with col1:
    ssc_p = st.number_input("SSC Percentage", min_value=0.0, max_value=100.0)
with col2:
    ssc_b_choice = st.selectbox("SSC Board", board_map)

col3, col4 = st.columns(2)
with col3:
    hsc_p = st.number_input("HSC Percentage", min_value=0.0, max_value=100.0)
with col4:
    hsc_b_choice = st.selectbox("HSC Board", board_map)

col5, col6 = st.columns(2)
with col5:
    hsc_subject_choice = st.selectbox("HSC Subject", hsc_subject_map)
with col6:
    degree_p = st.number_input("Degree Percentage", min_value=0.0, max_value=100.0)

col7, col8 = st.columns(2)
with col7:
    degree_type_choice = st.selectbox("Degree Type", degree_type_map)
with col8:
    workex_choice = st.selectbox("Work Experience", workexp_map)

col9, col10 = st.columns(2)
with col9:
    etest_p = st.number_input("E-test Percentage", min_value=0.0, max_value=100.0)
with col10:
    specialization_choice = st.selectbox("MBA Specialization", specialization_map)

mba_p = st.number_input("MBA Percentage", min_value=0.0, max_value=100.0)
gender_choice = st.selectbox("Gender", gender_map)

gender = gender_map[gender_choice]
ssc_b = board_map[ssc_b_choice]
hsc_b = board_map[hsc_b_choice]
workex = workexp_map[workex_choice]
specialization = specialization_map[specialization_choice]
hsc_subject = hsc_subject_map[hsc_subject_choice]
degree_type = degree_type_map[degree_type_choice]

if st.button("Predict Salary"):
    if any(val == 0.0 for val in [ssc_p, hsc_p, degree_p, etest_p, mba_p]):
        st.warning(" Please fill in all percentage fields with valid (non-zero) values.")
    else:
        try:
            input_data = [
                ssc_p,
                ssc_b,
                hsc_p,
                hsc_b,
                hsc_subject,
                degree_p,
                degree_type,
                workex,
                etest_p,
                specialization,
                mba_p,
                gender
            ]
            input_array = np.array(input_data).reshape(1, -1)
            salary = salary_model.predict(input_array)[0]
            st.success(f"💼 Predicted Salary: ₹{salary:,.2f}")
        except Exception as e:
            st.error(f"❌ Error during prediction: {str(e)}")

