from pathlib import Path

import streamlit as st

from src.ai_prediction import load_ai_model, predict_pollution_level
from src.prediction_repository import save_prediction
from src.treatment_optimization import (
    recommend_treatment,
    treatment_analysis
)
from src.gemini_explanation import generate_treatment_explanation


PROJECT_DIR = Path(__file__).resolve().parent

MODEL_PATH = PROJECT_DIR / "models" / "random_forest_model.pkl"

DATABASE_PATH = PROJECT_DIR / "data" / "wastewater_predictions.db"


# ----------------------------------------
# Load Random Forest Model
# ----------------------------------------

@st.cache_resource
def load_model():
    """Cache the trained Random Forest model."""
    return load_ai_model(MODEL_PATH)


# ----------------------------------------
# Page Configuration
# ----------------------------------------

st.set_page_config(
    page_title="Wastewater Treatment Optimization",
    page_icon="💧",
    layout="wide"
)


st.title(
    "Sustainable AI-Based Wastewater Treatment Optimization"
)

st.write(
    "Enter wastewater quality parameters to predict the pollution "
    "level and view the recommended treatment process."
)


# ----------------------------------------
# Check Model
# ----------------------------------------

if not MODEL_PATH.exists():

    st.error(
        f"Trained model not found: {MODEL_PATH}"
    )

    st.stop()


# ----------------------------------------
# Input Form
# ----------------------------------------

with st.form("water_quality_form"):

    column_one, column_two = st.columns(2)


    # ------------------------------------
    # Column One
    # ------------------------------------

    with column_one:

        ph = st.number_input(
            "pH",
            min_value=0.0,
            max_value=14.0,
            value=7.0,
            step=0.1
        )


        turbidity = st.number_input(
            "Turbidity (NTU)",
            min_value=0.0,
            value=1.0,
            step=0.1
        )


        temperature = st.number_input(
            "Temperature (°C)",
            min_value=0.0,
            value=25.0,
            step=0.1
        )


        dissolved_oxygen = st.number_input(
            "DO (mg/L)",
            min_value=0.0,
            value=5.0,
            step=0.1
        )


    # ------------------------------------
    # Column Two
    # ------------------------------------

    with column_two:

        bod = st.number_input(
            "BOD (mg/L)",
            min_value=0.0,
            value=5.0,
            step=0.1
        )


        lead = st.number_input(
            "Lead (mg/L)",
            min_value=0.0,
            value=0.0,
            step=0.0001,
            format="%.4f"
        )


        mercury = st.number_input(
            "Mercury (mg/L)",
            min_value=0.0,
            value=0.0,
            step=0.0001,
            format="%.4f"
        )


        arsenic = st.number_input(
            "Arsenic (mg/L)",
            min_value=0.0,
            value=0.0,
            step=0.0001,
            format="%.4f"
        )


    submitted = st.form_submit_button(
        "Predict Pollution Level and Optimize Treatment"
    )


# ----------------------------------------
# Prediction and Treatment
# ----------------------------------------

if submitted:

    # ------------------------------------
    # Prepare Input Values
    # ------------------------------------

    values = [
        ph,
        turbidity,
        temperature,
        dissolved_oxygen,
        bod,
        lead,
        mercury,
        arsenic
    ]


    # ------------------------------------
    # Random Forest Prediction
    # ------------------------------------

    model = load_model()

    predicted_level, predicted_label = predict_pollution_level(
        model,
        values
    )


    # ------------------------------------
    # Save Prediction to Database
    # ------------------------------------

    save_prediction(
        DATABASE_PATH,
        values,
        predicted_level
    )


    # ------------------------------------
    # Prediction Output
    # ------------------------------------

    st.subheader("Prediction")


    st.metric(
        "Predicted Pollution Level",
        predicted_label
    )


    # ------------------------------------
    # Treatment Recommendation
    # ------------------------------------

    recommended_steps = recommend_treatment(
        predicted_level,
        turbidity,
        bod,
        dissolved_oxygen,
        lead,
        mercury,
        arsenic
    )


    main_treatment, efficiency, energy = treatment_analysis(
        predicted_level
    )


    # ------------------------------------
    # Recommended Treatment Process
    # ------------------------------------

    st.subheader(
        "Recommended Treatment Process"
    )


    for index, step in enumerate(
        recommended_steps,
        start=1
    ):

        st.write(
            f"{index}. {step}"
        )


    # ------------------------------------
    # Treatment Analysis
    # ------------------------------------

    result_one, result_two, result_three = st.columns(3)


    result_one.metric(
        "Main Treatment",
        main_treatment
    )


    result_two.metric(
        "Estimated Efficiency",
        efficiency
    )


    result_three.metric(
        "Energy Consumption",
        energy
    )


    # ------------------------------------
    # Gemini Treatment Explanation
    # ------------------------------------

    gemini_parameters = {

        "pH": ph,

        "Turbidity (NTU)": turbidity,

        "Temperature (°C)": temperature,

        "DO (mg/L)": dissolved_oxygen,

        "BOD (mg/L)": bod,

        "Lead (mg/L)": lead,

        "Mercury (mg/L)": mercury,

        "Arsenic (mg/L)": arsenic
    }


    try:

        gemini_explanation = generate_treatment_explanation(
            predicted_label,
            gemini_parameters,
            recommended_steps
        )


        st.subheader(
            "Treatment Explanation"
        )


        st.markdown(
            gemini_explanation
        )


    except Exception as error:

        st.warning(
            "Treatment explanation is temporarily unavailable."
        )

        st.caption(
            f"Gemini service error: {error}"
        )


    # ------------------------------------
    # Information
    # ------------------------------------

    st.info(
        "The efficiency range and energy category are prototype "
        "decision-support estimates. They are not measured "
        "treatment-plant performance values."
    )