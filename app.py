import streamlit as st
import requests
import json
from pathlib import Path

st.set_page_config(page_title="ModelMind", page_icon="🧠", layout="wide")

st.title("🧠 ModelMind - ML Model Analyzer")
st.markdown("AI-powered model debugging with Gemini")
st.markdown("---")

# Check API health
try:
    response = requests.get("http://localhost:8000/health", timeout=2)
    if response.status_code == 200:
        st.success("✅ API Connected")
    else:
        st.error("❌ API Error")
except:
    st.error("❌ API not running. Start it with: python api.py")

st.markdown("---")

# Upload section
st.header("📤 Upload Model")

col1, col2 = st.columns(2)

with col1:
    model_file = st.file_uploader(
        "Select model file",
        type=["h5", "pt", "pth", "pkl"]
    )

with col2:
    logs_file = st.file_uploader(
        "Select logs (optional)",
        type=["txt", "csv", "json"]
    )

if st.button("🚀 Analyze", use_container_width=True):
    if not model_file:
        st.error("Please upload a model file")
    else:
        with st.spinner("Analyzing with Gemini..."):
            try:
                # Prepare files
                files = {
                    "model_file": model_file
                }
                
                if logs_file:
                    files["logs_file"] = logs_file
                
                # Send to API
                response = requests.post(
                    "http://localhost:8000/analyze",
                    files={
                        "model_file": (model_file.name, model_file.getvalue()),
                        "logs_file": (logs_file.name, logs_file.getvalue()) if logs_file else None
                    }
                )
                
                if response.status_code == 200:
                    result = response.json()
                    
                    st.success("✅ Analysis Complete!")
                    
                    # Display results
                    st.markdown("---")
                    st.header("📊 Results")
                    
                    # Model info
                    st.subheader("Model Information")
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Type", result["model_info"].get("type", "Unknown"))
                    with col2:
                        st.metric("Layers", result["model_info"].get("layers", "Unknown"))
                    with col3:
                        st.metric("Parameters", result["model_info"].get("parameters", "Unknown"))
                    
                    # Issues
                    if result["issues"]:
                        st.subheader("❌ Issues Found")
                        for issue in result["issues"]:
                            with st.expander(f"[{issue['severity']}] {issue['message']}"):
                                st.write(f"**Fix:** {issue['fix']}")
                    else:
                        st.success("No issues found!")
                    
                    # Analysis
                    st.subheader("🔍 Gemini Analysis")
                    st.write(result["analysis"])
                    
                    # Improvements
                    st.subheader("💡 Improvements")
                    st.write(result["improvements"])
                    
                    # Report
                    st.subheader("📄 Full Report")
                    with open(result["report_path"], 'r') as f:
                        report = f.read()
                    st.download_button(
                        "Download Report",
                        report,
                        file_name="analysis_report.txt"
                    )
                    
                else:
                    st.error(f"Error: {response.text}")
            
            except Exception as e:
                st.error(f"Error: {str(e)}")

st.markdown("---")
st.markdown("**ModelMind** - Stop guessing. Start knowing.")
