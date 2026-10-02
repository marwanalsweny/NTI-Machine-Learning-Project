NTI Machine Learning Project

Project Overview

This project was developed as part of my Machine Learning training at the National Telecommunication Institute (NTI).

The project focuses on predicting the Stress Level of children based on different factors related to their daily lifestyle, screen usage, activities, sleep, and surrounding environment.

The target variable is Stress_Levels, which represents three levels:

* Low
* Moderate
* High

The model uses different features such as:

* Age
* Daily Screen Time
* Device Dependency
* Gaming and device usage
* Hours of Sleep
* Physical Activity
* Parental Control
* Parental Involvement
* Extracurricular Activities
* Academic and social factors

The goal is to use these features to identify the child’s stress level using Machine Learning.

Project Workflow

The project follows a complete Machine Learning workflow:

1. Data Exploration and Analysis
2. Data Cleaning
3. Handling Missing Values
4. Data Preprocessing
5. Feature Encoding
6. Feature Selection
7. Model Training
8. Model Evaluation
9. Model Deployment
10. GUI Development

Machine Learning Model

The project uses a Random Forest Classifier to predict the child’s stress level.

Feature selection was performed using SelectKBest with ANOVA F-test (f_classif) to select the most relevant features before training the model.

Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Streamlit

Project Files

* NTI_Project.ipynb — Complete Machine Learning workflow, including data analysis, preprocessing, feature selection, model training, and evaluation.
* app.py — GUI application for making predictions.
* Model and preprocessing files — Saved components required for making predictions.
* Dataset — Dataset used for training and evaluation.

How to Run

Install the required libraries:

pip install -r requirements.txt

Then run the application:

streamlit run app.py

Project Highlights

This project demonstrates the complete Machine Learning pipeline, from exploring and preparing the data to selecting relevant features, training and evaluating the model, and finally deploying it through a user-friendly GUI.

The final application allows users to enter the relevant child-related features and receive a predicted Stress Level.

Disclaimer

This project is an educational Machine Learning project and is not intended to provide medical or psychological diagnosis.
