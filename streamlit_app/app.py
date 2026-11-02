import streamlit as st
from model_helper import predict
from PIL import Image
import os

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="AutoDamage AI",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------
st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #0B1220, #111827);
        color: white;
    }

        /* Remove Streamlit top header and empty space */
    [data-testid="stHeader"] {
        background: transparent;
        height: 0rem;
    }

    [data-testid="stToolbar"] {
        display: none;
    }

    .block-container {
    padding-top: 2rem !important;
    padding-bottom: 2rem;
    max-width: 1200px;
    }

    /* Remove Streamlit default padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    /* Hero Section */
    .hero-title {
        font-size: 4rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0;
        color: white;
    }

    .hero-title span {
        color: #38BDF8;
    }

    .hero-subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #CBD5E1;
        margin-top: 10px;
        margin-bottom: 40px;
    }

    /* Badge */
    .badge {
        display: inline-block;
        background: rgba(56, 189, 248, 0.15);
        color: #38BDF8;
        padding: 8px 18px;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 600;
        border: 1px solid rgba(56, 189, 248, 0.3);
    }

    /* Section headings */
    .section-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: white;
        margin-bottom: 10px;
    }

    .section-text {
        color: #94A3B8;
        font-size: 1rem;
        margin-bottom: 25px;
    }

    /* Prediction card */
    .prediction-card {
        background: linear-gradient(
            135deg,
            rgba(34, 197, 94, 0.15),
            rgba(16, 185, 129, 0.08)
        );
        border: 1px solid rgba(34, 197, 94, 0.4);
        border-radius: 15px;
        padding: 25px;
        text-align: center;
        margin-top: 20px;
    }

    .prediction-label {
        color: #94A3B8;
        font-size: 1rem;
    }

    .prediction-result {
        color: #22C55E;
        font-size: 2rem;
        font-weight: 700;
        margin-top: 10px;
    }

    /* Info cards */
    .info-card {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 15px;
        padding: 20px;
        height: 100%;
    }

    .info-card h3 {
        color: #38BDF8;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #64748B;
        margin-top: 60px;
        padding-top: 20px;
        border-top: 1px solid rgba(255,255,255,0.1);
    }

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------
st.markdown(
    """
    <div style="text-align:center;">
        <div class="badge">AI-POWERED VEHICLE ANALYSIS</div>
    </div>

    <h1 class="hero-title">
        AutoDamage <span>AI</span>
    </h1>

    <p class="hero-subtitle">
        Upload a vehicle image and let our AI analyze and classify its visible damage.
    </p>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# MAIN UPLOAD SECTION
# --------------------------------------------------
st.markdown('<div class="section-title">Analyze Your Vehicle</div>',
            unsafe_allow_html=True)

st.markdown(
    '<div class="section-text">Upload a clear image showing the front or rear of the vehicle.</div>',
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    "Upload vehicle image",
    type=["jpg", "jpeg", "png"],
    label_visibility="collapsed"
)


# --------------------------------------------------
# IMAGE + PREDICTION
# --------------------------------------------------
if uploaded_file is not None:

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("### 📷 Uploaded Image")

        image = Image.open(uploaded_file)
        st.image(image, width="stretch")

    with col2:
        st.markdown("### AI Analysis")

        st.write(
            "The AI model will analyze the uploaded vehicle image "
            "and classify its condition."
        )

        if st.button(
            "Analyze Vehicle",
            use_container_width=True,
            type="primary"
        ):

            image_path = "temp_file.jpg"

            with open(image_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            with st.spinner("Analyzing vehicle image..."):

                prediction = predict(image_path)

            st.markdown(
                f'<h2 style="color:#22C55E; font-weight:800;">{prediction}</h2>',
                unsafe_allow_html=True
            )

            if os.path.exists(image_path):
                os.remove(image_path)



# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("""
<div class="footer">
    <b>AutoDamage AI</b> · AI-Powered Vehicle Damage Classification
    <br><br>
    Proof of Concept · Computer Vision · Deep Learning
</div>
""", unsafe_allow_html=True)