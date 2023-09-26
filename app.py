import streamlit as st
import pandas as pd
import numpy as np

from src.pipelines.predict_pipeline import PredictPipeline

st.write("""
# Campus prediction App.

This app predicts whether the student will be recruited in campus placements or not based on the available factors in the dataset. 

Data obtained from [Kaggle campus placement](https://www.kaggle.com/competitions/ml-with-python-course-project/data)

""") 

st.sidebar.header('User Input Features')
st.sidebar.markdown("""
[Example CSV input file]()
""")

# Collects user input features into dataframe
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else:
    def user_input_features():
        GENDER = {'Male': 0, 'Female': 1}
        DEGREE_T = {'Science and Technology':'Sci&Tech', 'Commerece and Management': 'Comm&Mgmt', 'Others': 'Others'}
        SPECIALISATION= {'Market and HR': 'Mkt&HR', 'Market and Finance': 'Mkt&Fin'}
        gender = st.sidebar.selectbox('Gender', ('Male', 'Female'))
        ssc_p = st.sidebar.slider('Percentage of Mark scored in 10th', 0, 100, 40)
        ssc_b = st.sidebar.selectbox('Which Board Studied in 10th', ('Others', 'Central'))
        hsc_p = st.sidebar.slider('Percentage of Mark scored in 12th', 0, 100, 40)
        hsc_s = st.sidebar.selectbox('Which Stream Studied in 12th', ('Science', 'Commerce', 'Arts'))
        hsc_b = st.sidebar.selectbox('Which Board Studied in 12th', ('Others', 'Central'))
        degree_p = st.sidebar.slider('Percentage of Mark scored while completing Degree', 0, 100, 40)
        degree_t = st.sidebar.selectbox('Branch in which Degree was Acquired', ('Science and Technology', 'Commerece and Management', 'Others'))
        etest_p = st.sidebar.slider('Percentage of Mark scored placement exam', 0, 100, 40)
        workexp = st.sidebar.selectbox('Do you have prior work experience', ('yes', 'no'))
        mba_p = st.sidebar.slider('Percentage of Mark scored in MBA', 0, 100, 40)
        speci = st.sidebar.selectbox('Do you have specialization in any of the below criteria', ('Market and HR', 'Market and Finance'))
        gender_1 = GENDER[gender]
        degree_t_1 = DEGREE_T[degree_t]
        speci_1 = SPECIALISATION[speci]

        data = {
                'gender': gender_1,
                'ssc_p': ssc_p,
                'ssc_b': ssc_b,
                'hsc_p': hsc_p,
                'hsc_s': hsc_s,
                'hsc_b': hsc_b,
                'degree_p': degree_p,
                'degree_t': degree_t_1,
                'etest_p': etest_p,
                'workex': workexp,
                'mba_p': mba_p,
                'specialisation': speci_1
                }
        features = pd.DataFrame(data, index=[0])
        return features
    input_df = user_input_features()

st.subheader('User Input features')

if uploaded_file is not None:
    st.write(input_df)
else:
    st.write('Awaiting CSV file to be uploaded. Currently using example input parameters (shown below).')
    st.write(input_df)

predict_pipeline = PredictPipeline()

predicted_value= predict_pipeline.predict(input_df)

st.subheader('Prediction')
st.write('will be Placed' if predicted_value ==1 else 'Not placed')
