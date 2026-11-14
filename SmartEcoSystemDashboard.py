'''streamlit run SmartEcoSystemDashboard.py'''

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- Page Configuration & Elegant Theme ---
st.set_page_config(
    page_title="EcoSmart Campus Command Center",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Sleek Emerald/Dark Tech Dashboard
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        background-color: #1e293b;
        border-radius: 8px;
        color: white;
        padding: 10px 20px;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background-color: #10b981 !important;
        color: #000000 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Feature 4: Bilingual English / Arabic Toggle ---
st.sidebar.markdown("### 🌐 Language / اللغة")
lang = st.sidebar.radio("Select Language / اختر اللغة", ["English", "العربية"])

if lang == "العربية":
    title_text = "🌿 نظام كفاءة موارد الحرم الجامعي الذكي"
    sub_text = "جامعة ليوا | مسابقة الاستدامة الخامسة (خريف 2026-2027)"
    authors_text = "إعداد الطلاب: فاطمة فصيحة فايزور، ماديها فردوس شيخ | الإشراف: د. كرامات عتيق"
else:
    title_text = "🌿 Smart Campus Resource Efficiency System"
    sub_text = "Liwa University | 5th Sustainability Competition (Fall 2026-2027)"
    authors_text = "Project Authors: Fathima Faseeha Faizoor, Madiha Firdose Shiakh | Supervisor: Dr. Karamath Ateeq"

st.markdown(f"### 🏛️ {sub_text}")
st.title(title_text)
st.markdown(f"**{authors_text}**")
st.divider()

# --- Feature 1: Dynamic Sidebar Sliders & Real-Time Calculations ---
st.sidebar.header("🎛️ Live Scenario Simulator")
st.sidebar.markdown("Test options before investing, as recommended for campus decision-makers.")

window_mode = st.sidebar.selectbox(
    "Window Optimization Design" if lang=="English" else "تصميم تحسين النوافذ",
    ["Optimized (3x1 m with Louvers)", "Standard (5x3 m Large)"]
)
solar_spaces = st.sidebar.slider(
    "Covered Parking Spaces for Solar Canopy" if lang=="English" else "مواقف السيارات المغطاة بالطاقة الشمسية",
    50, 300, 150, 25
)
active_ac_monitors = st.sidebar.slider(
    "ESP32 Monitored Rooms" if lang=="English" else "الغرف المراقبَة بحساسات ESP32",
    10, 100, 50, 5
)

# Real-Time Mathematical Recalculations
is_optimized = "Optimized" in window_mode
peak_cooling_kw = 13.0 if is_optimized else 18.0  #
window_energy_saved_kwh = 7500 if is_optimized else 0  #

solar_gen_kwh = solar_spaces * 3600  # Dynamic annual scale yield
ac_waste_saved_kwh = active_ac_monitors * 420  # Proportional ESP32 savings

total_energy_saved = window_energy_saved_kwh + solar_gen_kwh + ac_waste_saved_kwh
total_co2_avoided = total_energy_saved * 0.00041  # Standard emission factor conversion
water_saved_m3 = 8760  #
landfill_reduced_t = 109.5  #

# --- Top Summary KPI Metrics ---
st.subheader("📊 Combined Annual Impact Summary (Live Updates)" if lang=="English" else "📊 ملخص التأثير السنوي المجمع (تحديث حي)")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="⚡ Net Energy Impact", value=f"{int(total_energy_saved):,} kWh", delta="+14.2%")
with col2:
    st.metric(label="🌍 CO₂ Avoided", value=f"{total_co2_avoided:.1f} t", delta="-18.5%")
with col3:
    st.metric(label="💧 Water Saved", value=f"{water_saved_m3:,} m³", delta="-30% reduction")
with col4:
    st.metric(label="♻️ Landfill Waste Reduced", value=f"{landfill_reduced_t} t", delta="15% → 45%")

st.divider()

# --- Feature 5: High-Impact Visual Progress Bars for Water & Recycling ---
st.subheader("💧 & ♻️ Resource Efficiency Progress Metrics" if lang=="English" else "💧 & ♻️ مقاييس تقدم كفاءة الموارد")
pcol1, pcol2 = st.columns(2)
with pcol1:
    st.markdown("**Smart Irrigation Water Reduction (Target: -30%)**")
    st.progress(0.30)
    st.caption("Reduced from 80,000 L/day down to 56,000 L/day (Saving 8,760 m³/year)")
with pcol2:
    st.markdown("**Smart Recycling Waste Diversion (Achieved: 45%)**")
    st.progress(0.45)
    st.caption("Successfully diverted 45% of campus waste away from landfills")

st.divider()

# --- 5 Detailed Interactive Modules Tabs ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🪟 1. Windows & Shading", 
    "🔌 2. Energy Monitoring", 
    "☀️ 3. Solar Canopy", 
    "♻️ 4. Smart Recycling", 
    "💧 5. Smart Irrigation"
])

with tab1:
    st.subheader("Window & Shading Optimization (Energy3D Simulation)")
    col_a, col_b = st.columns([2, 1])
    with col_a:
        st.markdown(f"""
        * **Problem:** Hot-climate campuses experience massive cooling loads from large windows.
        * **Solution:** Energy3D simulation tested reducing windows from **5×3 m to 3×1 m** with overhangs and louvers.
        * **Active Setting Peak Cooling:** **{peak_cooling_kw} kW** (vs 18 kW baseline).
        """)
        
        # --- Feature 3: Advanced Interactive Plotly Weather vs Cooling Chart ---
        hours = [f"{h:02d}:00" for h in range(24)]
        std_cooling = [0.5, 0.6, 0.8, 1.0, 1.5, 3.0, 11.0, 16.0, 18.0, 18.8, 18.5, 17.0, 17.0, 18.2, 19.0, 18.2, 13.0, 4.5, 2.0, 1.5, 1.2, 1.0, 0.8, 0.6]
        opt_cooling = [val * (13.0/18.0) if is_optimized else val for val in std_cooling]
        
        df_chart = pd.DataFrame({
            "Hour": hours,
            "Cooling Load (kW)": opt_cooling,
            "Design Type": window_mode
        })
        
        fig = px.area(
            df_chart, x="Hour", y="Cooling Load (kW)", 
            title="Abu Dhabi Hourly Cooling Load Analysis (May 2)",
            color_discrete_sequence=["#10b981" if is_optimized else "#f43f5e"]
        )
        fig.update_layout(
            plot_bgcolor="#0e1117", paper_bgcolor="#0e1117", font_color="white",
            xaxis=dict(showgrid=True, gridcolor="#1e293b"),
            yaxis=dict(showgrid=True, gridcolor="#1e293b")
        )
        st.plotly_chart(fig, use_container_width=True)
        
    with col_b:
        st.info("📌 **Simulation Insight**\n\nOptimized 3×1 m windows cut peak cooling load from **18 kW to 13 kW**, saving approximately **7,500 kWh** annually.")

with tab2:
    st.subheader("ESP32 Occupancy & Current Monitoring")
    st.markdown("""
    * **Technology:** ESP32 microcontrollers with current and occupancy sensors.
    * **Function:** Detects empty rooms and automatically shuts down air conditioning to eliminate wasted electricity.
    """)
    
    # --- Feature 2: Energy Waste Visualizer ("Rooms Turn Red / Green") ---
    st.markdown("### 🏢 Live Campus Floor Plan - Room Status Grid")
    rcol1, rcol2, rcol3 = st.columns(3)
    
    with rcol1:
        st.markdown("**Lecture Hall 101**")
        waste_101 = st.checkbox("Simulate Empty + AC Waste (101)", value=True, key="w101")
        if waste_101:
            st.error("⚠️ EMPTY ROOM: AC running wasting energy!")
        else:
            st.success("✅ Optimized / Occupied normally")
            
    with rcol2:
        st.markdown("**Computer Lab 203**")
        waste_203 = st.checkbox("Simulate Empty + AC Waste (203)", value=False, key="w203")
        if waste_203:
            st.error("⚠️ EMPTY ROOM: AC running wasting energy!")
        else:
            st.success("✅ Optimized / Occupied normally")
            
    with rcol3:
        st.markdown("**Faculty Office 302**")
        waste_302 = st.checkbox("Simulate Empty + AC Waste (302)", value=True, key="w302")
        if waste_302:
            st.error("⚠️ EMPTY ROOM: AC running wasting energy!")
        else:
            st.success("✅ Optimized / Occupied normally")

with tab3:
    st.subheader("Solar Canopy Yield over Parking Spaces")
    scol1, scol2 = st.columns(2)
    with scol1:
        st.metric("Total Solar Capacity", f"{solar_spaces * 2.5:.1f} kWp")
        st.metric("Covered Parking Spaces", f"{solar_spaces} Spaces")
    with scol2:
        st.metric("Annual Clean Energy Generation", f"{int(solar_gen_kwh):,} kWh")
        st.markdown("Provides clean renewable energy for campus buildings while offering essential shade for cars in Abu Dhabi's hot climate.")

with tab4:
    st.subheader("Smart Recycling & Fill-Level Bins")
    st.markdown("""
    * **Audit Results:** Upgraded campus sorting infrastructure with fill-level smart bins.
    * **Diversion Rate:** Increased waste diversion from **15% up to 45%**.
    * **Landfill Reduction:** Diverts **109.5 tonnes** of waste away from landfills annually.
    """)
    
    rec_df = pd.DataFrame({
        "Stage": ["Before Project", "Current Target"],
        "Diversion Rate (%)": [15, 45]
    })
    fig_rec = px.bar(rec_df, x="Stage", y="Diversion Rate (%)", color="Stage", color_discrete_map={"Before Project": "#f43f5e", "Current Target": "#10b981"})
    fig_rec.update_layout(plot_bgcolor="#0e1117", paper_bgcolor="#0e1117", font_color="white")
    st.plotly_chart(fig_rec, use_container_width=True)

with tab5:
    st.subheader("Smart Irrigation (Soil Moisture & Weather Scheduling)")
    st.markdown("""
    * **Water Reduction:** Cut water usage by **30%**.
    * **Volume Shift:** Reduced consumption from **80,000 L/day down to 56,000 L/day**.
    * **Total Savings:** Saves **8,760 m³** of water per year through intelligent weather-based scheduling.
    """)
    wcol1, wcol2 = st.columns(2)
    wcol1.metric("Baseline Irrigation", "80,000 L / day")
    wcol2.metric("Optimized Smart Irrigation", "56,000 L / day (-30%)")

# --- Footer Recommendation ---
st.divider()
st.markdown("""
### 🚀 Project Recommendations & Next Steps
1. **Pilot Phase:** Deploy in one campus building first to replace estimations with live measured sensor data.
2. **Localization:** Fully integrated bilingual Arabic/English dynamic support.
""")