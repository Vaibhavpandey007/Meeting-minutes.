import streamlit as st
import sys
import os

# Add the src directory to the path so we can import the summarizer
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.summarizer import summarize_text

# Page Configuration
st.set_page_config(
    page_title="Meeting Minutes AI",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding-top: 2rem;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #FF4B4B;
        color: white;
    }
    .stTextArea>div>div>textarea {
        border-radius: 5px;
    }
    .css-1d391kg {
        padding-top: 3.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1250/1250689.png", width=100)
    st.title("Meeting Minutes AI")
    st.markdown("---")
    st.markdown("""
    **How to use:**
    1. Upload a meeting transcript (txt) OR paste the text.
    2. Click **Generate Minutes**.
    3. View and download your summary.
    """)
    st.markdown("---")
    st.markdown("Built with ❤️ using [Streamlit](https://streamlit.io) and Transformers.")

# Main Content
st.title("📝 Meeting Minutes Generator")
st.markdown("Transform your long meeting transcripts into concise summaries and actionable items in seconds.")

# Input Section
st.markdown("### 📥 Input Transcript")
tab1, tab2 = st.tabs(["📂 Upload File", "✍️ Paste Text"])

text_to_summarize = ""

with tab1:
    uploaded_file = st.file_uploader("Choose a transcript file (.txt)", type="txt")
    if uploaded_file is not None:
        text_to_summarize = uploaded_file.read().decode("utf-8")
        st.success("File uploaded successfully!")

with tab2:
    text_input = st.text_area("Paste your transcript here...", height=300)
    if text_input:
        text_to_summarize = text_input

# Generate Button
if st.button("Generate Minutes ✨", type="primary"):
    if text_to_summarize:
        with st.spinner("🤖 Analyzing transcript and generating minutes..."):
            try:
                # Generate minutes
                minutes = summarize_text(text_to_summarize)
                
                # Display Results
                st.markdown("---")
                st.markdown("## 📊 Meeting Minutes")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("📋 Executive Summary")
                    st.info(minutes["executive_summary"])
                    
                with col2:
                    st.subheader("✅ Action Items")
                    st.success(minutes["action_items"])
                
                # Download Button
                report_text = f"""Meeting Minutes Report
----------------------

Executive Summary:
{minutes['executive_summary']}

Action Items:
{minutes['action_items']}
"""
                st.download_button(
                    label="📥 Download Report",
                    data=report_text,
                    file_name="meeting_minutes.txt",
                    mime="text/plain"
                )
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("⚠️ Please upload a file or enter text to proceed.")
