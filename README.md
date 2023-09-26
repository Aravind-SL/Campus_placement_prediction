# Campus Placements Prediction Web App

## Introduction

The Campus Placements Prediction Web App is a tool designed to predict the likelihood of a student getting placed during campus placements based on various factors such as academic performance, skills, and other relevant data. This web app is trained and works as per the given dataset this can be easily modified based on the needs of recruiter.

## Features

- **Prediction**: Predicts the probability of a student getting placed during campus placements.
- **User-Friendly Interface**: The web app provides an intuitive and easy-to-use interface.
- **Data Visualization**: Visualize the data used for predictions.
- **Customizable Model**: The machine learning model used for prediction can be customized based on the available data.
- **Scalability**: The web app can be easily scaled to handle a large number of users and data.

## Description About Data

- **sl_no**: anonymous id unique to a given employee
- **gender**: employee gender
- **ssc_p**: SSC is Secondary School Certificate (Class 10th). ssc_p is the percentage of marks secured in Class 10th.
- **ssc_b**: SSC Board. Binary feature.
- **hsc_p**: HSC is Higher Secondary Certificate (Class 12th). hsc_p is the percentage of marks secured in Class 12th.
- **hsc_b**: HSC Board. Binary feature.
- **hsc_s**: HSC Subject. Feature with three categories.
- **degree_p**: percentage of marks secured while acquiring the degree.
- **degree_t**: branch in which the degree was acquired. Feature with three categories.
- **workex**: Whether the employee has some work experience or not. Binary feature.
- **etest_p**: percentage of marks secured in the placement exam.
- **specialisation**: the specialization that an employee has. Binary feature.
- **mba_p**: percentage of marks secured by an employee while doing his MBA.
- **status**: whether the student was placed or not. Binary Feature. Target variable.
- **salary**: annual compensation at which an employee was hired.

## How to Use
1. App link [Streamlit prediction app](https://campus-placements.streamlit.app/)

## Data Source
The dataset used for this project can be found at [kaggle campus placement data](https://www.kaggle.com/competitions/ml-with-python-course-project/data).

## Note
This project is for educational and demonstration purposes only. The predictions may not reflect actual market conditions.
