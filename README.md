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
<img width="1920" height="875" alt="Screenshot 2026-10-02 072610" src="https://github.com/user-attachments/assets/c3110378-c8fc-41ff-9b0b-c056bb71d37a" />
<img width="1901" height="891" alt="Screenshot 2026-10-02 072533" src="https://github.com/user-attachments/assets/163582fc-19c3-4797-a939-f1fbae252a2b" />
<img width="1867" height="893" alt="Screenshot 2026-10-02 072456" src="https://github.com/user-attachments/assets/c81a98d1-d06b-434e-b890-afe0e587f4c4" />
<img width="1871" height="897" alt="Screenshot 2026-10-02 072630" src="https://github.com/user-attachments/assets/6a50fbca-2d2f-4c94-98c1-1726f0186e48" />


