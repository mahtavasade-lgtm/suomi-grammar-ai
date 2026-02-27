import streamlit as st
from openai import OpenAI
import base64

# Streamlit Secrets ကနေ API Key ကို ခေါ်သုံးခြင်း
try:
    api_key = st.secrets["OPENAI_API_KEY"]
except:
    st.error("ကျေးဇူးပြု၍ Streamlit Settings ထဲမှာ API Key ထည့်ပေးပါ!")
    st.stop()

client = OpenAI(api_key=api_key)

st.set_page_config(page_title="Suomi-Myanmar Grammar AI", layout="wide")
st.title("🇫🇮 Suomi-Myanmar သဒ္ဒါလက်ထောက်")

# Photo input
img_file = st.camera_input("ဖင်လန်စာပါတဲ့ စာမျက်နှာကို ဓာတ်ပုံရိုက်ပါ")

if img_file:
    with st.spinner('AI က ဇယားဆွဲပေးနေပါတယ်...'):
        # Encode image to base64
        base64_image = base64.b64encode(img_file.getvalue()).decode('utf-8')
        
        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "You are a Finnish-Burmese grammar expert. For any Finnish word, create a markdown table with 3 columns: Finnish form, Myanmar meaning, and Grammar category. Include Basic forms (Infinitive, Noun, Genitive, Passive) and Person-based forms (Minä, Sinä, etc.) with Burmese suffixes 'သည်' for verbs and 'ခြင်း/၏' for nouns."
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Analyze the Finnish words in this image and provide grammar tables in Burmese."},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                    ],
                }
            ]
        )
        st.markdown(response.choices[0].message.content)
