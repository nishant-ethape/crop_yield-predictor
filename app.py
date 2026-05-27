import streamlit as st
import requests
from predictor import valid_crops, valid_states

# Page config
st.set_page_config(
    page_title="Krishi Yield Predictor",
    page_icon="🌾",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
    
    * { font-family: 'Poppins', sans-serif; }
    
    .main { background: linear-gradient(135deg, #f5f7fa 0%, #c3e6cb 100%); }
    
    .hero {
        background: linear-gradient(135deg, #1a6b3c, #2ecc71);
        padding: 2.5rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(46,204,113,0.3);
    }
    
    .hero h1 {
        color: white;
        font-size: 2.8rem;
        font-weight: 700;
        margin: 0;
    }
    
    .hero p {
        color: rgba(255,255,255,0.85);
        font-size: 1.1rem;
        margin-top: 0.5rem;
    }
    
    .card {
        background: white;
        border-radius: 16px;
        padding: 1.8rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        margin-bottom: 1rem;
    }
    
    .section-title {
        color: #1a6b3c;
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 1rem;
        border-left: 4px solid #2ecc71;
        padding-left: 0.8rem;
    }
    
    .result-box {
        background: linear-gradient(135deg, #1a6b3c, #27ae60);
        border-radius: 16px;
        padding: 2rem;
        text-align: center;
        color: white;
        box-shadow: 0 8px 25px rgba(26,107,60,0.4);
    }
    
    .result-number {
        font-size: 3rem;
        font-weight: 700;
        color: #2ecc71;
    }
    
    .result-label {
        font-size: 0.95rem;
        color: rgba(255,255,255,0.8);
        margin-top: 0.3rem;
    }
    
    .marathi-text {
        color: #666;
        font-size: 0.85rem;
        margin-top: 0.2rem;
    }

    .stButton>button {
        background: linear-gradient(135deg, #1a6b3c, #2ecc71);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.8rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        width: 100%;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(46,204,113,0.4);
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(46,204,113,0.5);
    }

    .tip-box {
        background: #ffd54e;
        border: 1px solid #f39c12;
        border-radius: 12px;
        padding: 1rem 1.2rem;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Hero section
st.markdown("""
<div class="hero">
    <h1>🌾 Krishi Yield Predictor</h1>
    <p>Crop Yield Prediction for Indian Farmers | भारतीय शेतकऱ्यांसाठी पीक उत्पादन अंदाज</p>
</div>
""", unsafe_allow_html=True)

# Layout
col1, col2 = st.columns([1.2, 1], gap="large")

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🌱 Crop Details | पीक माहिती</div>', unsafe_allow_html=True)

    crop = st.selectbox("Select Crop | पीक निवडा", valid_crops)
    state = st.selectbox("Select State | राज्य निवडा", valid_states)
    
    season_map = {
        "Kharif (खरीप)": "Kharif",
        "Rabi (रब्बी)": "Rabi", 
        "Summer (उन्हाळी)": "Summer",
        "Whole Year (वार्षिक)": "Whole Year"
    }
    season_display = st.selectbox("Select Season | हंगाम निवडा", list(season_map.keys()))
    season = season_map[season_display]
    
    year = st.number_input("Year | वर्ष", min_value=1997, max_value=2030, value=2024)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🌧️ Field Details | शेत माहिती</div>', unsafe_allow_html=True)
    
    area = st.number_input("Land Area in Hectares | जमीन क्षेत्र (हेक्टर)", min_value=0.1, value=1.0)
    rainfall = st.number_input("Annual Rainfall in mm | वार्षिक पाऊस (मिमी)", min_value=0.0, value=1000.0)
    fertilizer = st.number_input("Fertilizer Used in kg | खत वापर (किलो)", min_value=0.0, value=100.0)
    pesticide = st.number_input("Pesticide Used in kg | कीटकनाशक (किलो)", min_value=0.0, value=10.0)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📊 Prediction | अंदाज</div>', unsafe_allow_html=True)

    if st.button("🌾 Predict Yield | उत्पादन अंदाज करा"):

        response = requests.post("http://localhost:8000/predict", json={
    # send raw form values as dictionary
    'crop': crop,
    'season': season,
    'state':state,
    'year': year,
    'rainfall': rainfall,
    'area': area,
    'fertilizer': fertilizer,
    'pesticide': pesticide
})

        result = response.json()

        predicted_yield = result["predicted_yield"]
        total_production = result["total_production"]
        total_quintals = result["total_quintals"]

        st.markdown(f"""
        <div class="result-box">
            <div style="font-size:1rem; color:rgba(255,255,255,0.8)">Predicted Yield | अंदाजित उत्पादन</div>
            <div class="result-number">{predicted_yield:.2f}</div>
            <div class="result-label">tonnes per hectare | टन प्रति हेक्टर</div>
            <br>
            <div style="font-size:1rem; color:rgba(255,255,255,0.8)">Total Expected Production</div>
            <div style="font-size:2rem; font-weight:700; color:#a8f0c6">{total_production:.2f} tonnes</div>
            <div class="result-label">{total_quintals:.1f} quintals | क्विंटल</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="tip-box">
            💡 <strong>Tip:</strong> {crop} in {state} during {season} season 
            with {area} hectares is expected to yield 
            <strong>{total_quintals:.1f} quintals</strong> total.
            <div class="marathi-text">
            {crop} पीक {state} मध्ये {season_display.split('(')[1].replace(')', '')} हंगामात 
            {area} हेक्टरमध्ये अंदाजे <strong>{total_quintals:.1f} क्विंटल</strong> उत्पादन देईल.
            </div>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown("""
        <div style="text-align:center; padding:3rem; color:#aaa;">
            <div style="font-size:4rem">🌱</div>
            <div style="font-size:1.1rem; margin-top:1rem">
                Fill in the details and click predict
            </div>
            <div style="font-size:0.9rem; color:#bbb; margin-top:0.5rem">
                माहिती भरा आणि अंदाज करा
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Footer info
    st.markdown("""
    <div class="card" style="margin-top:1rem">
        <div class="section-title">ℹ️ About | बद्दल</div>
        <p style="color:#555; font-size:0.9rem">
        This model is trained on 15,000+ records from the Ministry of Agriculture 
        covering 37 crops across 30 Indian states from 1997-2021. 
        Accuracy: <strong>97.3% R²</strong>
        </p>
        <p style="color:#888; font-size:0.8rem">
        हे मॉडेल कृषी मंत्रालयाच्या १५,००० + नोंदींवर प्रशिक्षित आहे.
        </p>
    </div>
    """, unsafe_allow_html=True)