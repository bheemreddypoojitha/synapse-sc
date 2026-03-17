import streamlit as st
import time
from ai_swarm import run_synapse_swarm

# --- UI Configuration ---
st.set_page_config(page_title="SYNAPSE-SC | Enterprise Hub", layout="wide", page_icon="🌐")

# Custom CSS for "Enterprise Dark Mode"
st.markdown("""
    <style>
    .main {background-color: #0E1117;}
    h1 {color: #00E5FF;} 
    .metric-box {background-color: #1E2127; padding: 20px; border-radius: 10px; border-left: 5px solid #00E5FF;}
    .metric-box h3 {color: #FFFFFF;} 
    .metric-box h2 {color: #FFFFFF;}
    .success-text {color: #00FF00; font-weight: bold;}
    </style>
""", unsafe_allow_html=True)

st.title("🌐 SYNAPSE-SC")
st.subheader("Autonomous Supply Chain Risk & Mitigation Engine")

# --- Dashboard Metrics ---
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="metric-box"><h3>Active Supply Nodes</h3><h2>1,402</h2></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-box"><h3>Global Alerts</h3><h2 style="color: #FF4B4B;">1 Critical</h2></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="metric-box"><h3>Autonomous Reroutes</h3><h2 style="color: #00FF00;">System Ready</h2></div>', unsafe_allow_html=True)

st.divider()

# --- The Demo Execution ---
st.write("### 🧠 Multi-Agent Simulation")
st.write("Initiate the AI swarm to scan global APIs, model ERP impact, and execute rerouting protocols.")

if st.button("🚀 INITIATE AUTONOMOUS RISK SCAN", type="primary", use_container_width=True):
    
    # Visual loading effect for the pitch video
    with st.status("Executing Multi-Agent Workflow...", expanded=True) as status:
        st.write("📡 **Agent 1 (Sentinel):** Pinging global weather and logistics APIs...")
        
        # ACTUALLY RUN THE AI SWARM (This takes ~10 seconds)
        try:
            final_result = run_synapse_swarm()
            
            st.write("💾 **Agent 2 (Quant):** Alert detected. Querying SAP/ERP for inventory at risk...")
            time.sleep(1) # Small delay for UI smoothness
            st.write("⚖️ **Agent 3 (Orchestrator):** Calculating mitigation costs against $10,000 compliance guardrail...")
            time.sleep(1)
            
            status.update(label="✅ Workflow Complete: Action Taken", state="complete", expanded=False)
            
            st.success("Autonomous Rerouting Executed Successfully within Guardrails.")
            
            st.write("### 📄 Final Audit Trail & Orchestrator Output")
            st.info(final_result)
            
            st.write("### 💸 Business Impact of this action:")
            st.code("""
            PREDICTED LOSS AVOIDED: $15,000 (3 days of SLA penalties)
            REROUTE COST: $4,500 (Rail-Express)
            NET ENTERPRISE SAVINGS: $10,500
            TIME TO RESOLUTION: < 15 Seconds
            """, language="markdown")
            
        except Exception as e:
            status.update(label="❌ Error in execution", state="error", expanded=True)
            st.error(f"Failed to run swarm: {e}")
            st.write("Ensure your Groq API key is correct in the .env file.")