import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title="Child Stress Assessment", layout="centered")

@st.cache_resource
def load_engine():
    m = joblib.load('/content/rf_model_file.joblib')
    enc = joblib.load('/content/onehot_encoder_file.joblib')
    sel = joblib.load('/content/selector_file.joblib')
    return m, enc, sel

model, encoder, selector = load_engine()

st.title("Child Stress Risk Assessment")
st.caption("Interactive behavioral and routine evaluation")
st.divider()

col1, col2 = st.columns(2)
with col1:
    age = st.slider("Child Age (Years)", 2.0, 13.0, 7.0, 0.5)
    sleep = st.slider("Daily Sleep Duration (Hours)", 4.0, 12.0, 8.5, 0.25)
    screen = st.slider("Daily Screen Time (Hours)", 0.0, 16.0, 4.0, 0.5)

with col2:
    dep = st.slider("Device Dependency Level (1 - 10)", 1.0, 10.0, 5.0, 0.5)
    strict = st.slider("Parental Supervision Level (1 - 10)", 1.0, 10.0, 5.0, 0.5)
    emot = st.selectbox("Reaction to Device Removal", ["Neutral", "Distressed", "Irritable", "Unbothered"])
    acad = st.selectbox("Academic Trend", ["Positive", "Neutral", "Negative"])

st.divider()

if st.button("Evaluate Stress Profile", use_container_width=True):
    acad_map = {"Negative": 0, "Neutral": 1, "Positive": 2}
    
    x_num = np.array([
        age, screen, dep, strict, acad_map.get(acad, 1),
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, sleep
    ]).reshape(1, -1)

    cat_df = pd.DataFrame([{
        "Preferred_Activity": "Gaming",
        "Emotional_Response_To_No_Device": emot,
        "Social_Interactions_Preference": "Balanced",
        "Gender": "Male",
        "Teacher_Feedback": "Moderate",
        "Favorite_Subject": "Science"
    }])

    x_cat = encoder.transform(cat_df)
    if hasattr(x_cat, "toarray"):
        x_cat = x_cat.toarray()

    x_full = np.hstack([x_num, x_cat])
    x_sel = selector.transform(x_full)

    pred = str(model.predict(x_sel)[0])
    probs = model.predict_proba(x_sel)[0]

    st.subheader("Assessment Result:")
    if pred.lower() in ["low", "0"]:
        st.success("Predicted Status: Low Stress")
    elif pred.lower() in ["moderate", "1"]:
        st.warning("Predicted Status: Moderate Stress")
    else:
        st.error("Predicted Status: High Stress")

    st.write("Classification Confidence:")
    for c, p in zip(model.classes_, probs):
        lbl = "Low" if str(c).lower() in ["low", "0"] else ("Moderate" if str(c).lower() in ["moderate", "1"] else "High")
        st.write(f"{lbl}: {p*100:.1f}%")
        st.progress(float(p))
