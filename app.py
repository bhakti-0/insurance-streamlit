import streamlit as st
import pickle

with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age:", min_value=0, step=1, format="%d", value=25)
        children = st.number_input("Children:", min_value=0, step=1, format="%d", value=0)
        gender = st.radio("Gender:", ["Male", "Female"], horizontal=True)

    with col2:
        bmi = st.number_input("BMI:", min_value=10.0, max_value=100.0, step=0.1, format="%.1f", value=25.0)
        smoker = st.radio("Do you smoke?", ["Yes", "No"], horizontal=True)

    # ✅ Only one submit button
    submitted = st.form_submit_button("🔮 Predict Premium")

# Load model
model = pickle.load(open('model.pkl','rb'))

if submitted:  # Run only when form is submitted
    gender_enc = 0 if gender.upper() == 'MALE' else 1
    smoker_enc = 0 if smoker.upper() == 'NO' else 1 
    x_test = [[age, bmi, children, gender_enc, smoker_enc]]
    yp = str(round(model.predict(x_test)[0], 2))
    st.success('💰 Your Premium is: ' + yp)


